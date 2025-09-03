import asyncio
from playwright.async_api import async_playwright
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from apify_client import ApifyClient

load_dotenv()

# Config
EVENT_URL = os.environ.get("EVENT_URL")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")
TARGET_PRICE = float(os.environ.get("TARGET_PRICE"))
APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
apify_client = ApifyClient(APIFY_TOKEN)
STORE_NAME = "LAST_ALERTED_PRICE_STORE"
LAST_PRICE_KEY = "last_price"
print(f"Target price set to: ${TARGET_PRICE}")
print(f"Event URL: {EVENT_URL}")
print(f"Discord Webhook: {DISCORD_WEBHOOK}")
print(f"Apify Store: {STORE_NAME}, Key: {LAST_PRICE_KEY}")
print(f"Apify Token: {'Set' if APIFY_TOKEN else 'Not Set'}")


async def fetch_prices():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        await page.goto(EVENT_URL, timeout=60000)
        try:
            await page.wait_for_selector("#quickpick-buy-button-qp-0", timeout=30000)
        except Exception as e:
            print(f"Selector not found: {e}")
            await browser.close()
            return []

        # html_content = await page.content()
        # await browser.close()
        price_txt = await page.inner_text("#quickpick-buy-button-qp-0")
        await browser.close()

        # soup = BeautifulSoup(html_content, "html.parser")
        # events = soup.find_all("span", class_="sc-366ff4a8-1.bQzoso")

        prices = []
        try:
            clean_txt = price_txt.replace("$", "").replace(",", "").strip()
            prices.append(float(clean_txt))
        except ValueError:
            pass
    return prices


# def check_last_alerted_price():
#     if not os.path.exists("last_alerted_price.json"):
#         return 0.0
#     with open("last_alerted_price.json", "r") as file:
#         data = json.load(file)
#     return data.get("last_price", 0.0)
def get_last_alerted_price():
    try:
        record = apify_client.key_value_stores.get_record(STORE_NAME, LAST_PRICE_KEY)
        return float(record["value"]) if record else 0.0
    except Exception as e:
        print(f"Error fetching last alerted price: {e}")
        return 0.0

def update_last_alerted_price(price):
    try:
        apify_client.key_value_stores.set_record(STORE_NAME, LAST_PRICE_KEY, {"value": price})
    except Exception as e:
        print(f"Error updating last alerted price: {e}")


def send_discord_alert(message: str):
    try:
        resp = requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=10)
        if resp.status_code != 204:
            print(f"Discord webhook failed: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Error sending Discord alert: {e}")


async def check_prices():
    prices = await fetch_prices()
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

def send_daily_checkin():
    lowest_price = fetch_prices()[0] if fetch_prices() else 0.0
    if lowest_price > 0.0:
        send_discord_alert(f"🤑 The lowest ticket price rn is **${lowest_price}**\n{EVENT_URL}")
    else:
        send_discord_alert("🤑 No ticket price data yet")


def check_time():
    current_time = datetime.now()
    target_hour = 22  # 10 PM

    if current_time.hour == target_hour:
        send_daily_checkin()
        return


if __name__ == "__main__":
    asyncio.run(check_prices())
    check_time()