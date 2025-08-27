import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Config from GitHub Secrets
EVENT_URL = os.environ.get("EVENT_URL")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")
TARGET_PRICE = 800  # Your desired alert threshold

async def fetch_prices():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(EVENT_URL)
        await page.wait_for_selector("span.sc-366ff4a8-1.bQzoso")
        html_content = await page.content()
        await browser.close()

        soup = BeautifulSoup(html_content, "html.parser")
        events = soup.find_all("span", class_="sc-366ff4a8-1 bQzoso")

        prices = []
        for event in events:
            try:
                price_text = event.text.replace("$", "").replace(",", "")
                price = float(price_text)
                prices.append(price)
            except ValueError:
                continue
        return prices

def send_discord_alert(price):
    data = {"content": f"🎸 Ticket available for ${price}! {EVENT_URL}"}
    requests.post(DISCORD_WEBHOOK, json=data)

async def check_prices():
    prices = await fetch_prices()
    if not prices:
        print("No prices found.")
        return

    lowest_price = min(prices)
    print(f"Lowest price found: ${lowest_price}")

    if lowest_price <= TARGET_PRICE:
        send_discord_alert(lowest_price)
        print(f"Alert sent for ${lowest_price}!")
    else:
        print("No alert needed.")

if __name__ == "__main__":
    asyncio.run(check_prices())