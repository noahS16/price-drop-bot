import asyncio
from playwright.async_api import async_playwright
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from apify_client import ApifyClient
from apify import Actor


load_dotenv()

# Config
EVENT_URL = os.environ.get("EVENT_URL")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")
TARGET_PRICE = float(os.environ.get("TARGET_PRICE", "300"))

print(f"Target price set to: ${TARGET_PRICE}")
print(f"Event URL: {EVENT_URL}")
print(f"Discord Webhook: {DISCORD_WEBHOOK}")

async def setup_proxy():
    proxy_config = await Actor.create_proxy_configuration(
        groups= ["RESIDENTIAL"],
        country_code= 'US',
    )
    if not proxy_config:
        print("Failed to create proxy configuration.")
        return None
    proxy_url = await proxy_config.new_url()
    Actor.log.info(f'Using proxy URL: {proxy_url}')
    return proxy_url

async def fetch_prices(proxy_url):
    print(f"Proxy URL: {proxy_url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=Actor.config.headless, 
            args=['--disable-gpu'],
            proxy=proxy_url,
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"},
        )

        page = await context.new_page()

        await page.goto(EVENT_URL, wait_until='networkidle', timeout=60000)
        html = await page.content()
        print(html[:2000])  # first 2000 chars

        try:
            await page.wait_for_selector("#quickpick-buy-button-qp-0", timeout=30000)
        except Exception as e:
            print(f"Selector not found: {e}")
            await browser.close()
            return []

        price_txt = await page.inner_text("#quickpick-buy-button-qp-0")
        await browser.close()

        prices = []
        try:
            clean_txt = price_txt.replace("$", "").replace(",", "").strip()
            prices.append(float(clean_txt))
        except ValueError:
            pass
    return prices


def send_discord_alert(message: str):
    try:
        resp = requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=10)
        if resp.status_code != 204:
            print(f"Discord webhook failed: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Error sending Discord alert: {e}")


async def check_prices(proxy_url):
    prices = await fetch_prices(proxy_url)
    if not prices:
        print("No prices found.")
        send_discord_alert("⚠️ No ticket prices found! LOCK IN!! ‼️")
        return

    lowest_price = min(prices)
    #last_alerted_price = get_last_alerted_price()
    print(f"Lowest price found: ${lowest_price}")

    if lowest_price <= TARGET_PRICE or lowest_price <= 300.0:
        send_discord_alert(f"🎸 Ticket available for **${lowest_price}**!\n{EVENT_URL}")
        #update_last_alerted_price(lowest_price)
        print(f"Alert sent for ${lowest_price}!")
    else:
        print("No alert needed.")

async def send_daily_checkin():
    prices = await fetch_prices()
    lowest_price = prices[0] if prices else None
    if lowest_price:
        send_discord_alert(f"🤑 The lowest ticket price rn is **${lowest_price}**\n{EVENT_URL}")
    else:
        send_discord_alert("🤑 No ticket price data yet")


def check_time():
    current_time = datetime.now()
    target_hour = 22  # 10 PM
    if current_time.hour == target_hour:
       asyncio.run(send_daily_checkin)

async def main() -> None:
    async with Actor:
        proxy_url = {"server": await setup_proxy()} if os.environ.get("USE_PROXY", "true").lower() == "true" else None
        await check_prices(proxy_url)
        check_time()

if __name__ == "__main__":
    asyncio.run(main())
