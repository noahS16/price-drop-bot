import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests
import json
import os
from google.cloud import firestore

# Config
EVENT_URL = os.environ.get("EVENT_URL")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")
TARGET_PRICE = 800  # Your desired alert threshold
ALERT_FILE = "alerts.json"

db = firestore.Client()
doc = db.collection("alerts").document("the strokes")

async def fetch_prices():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(EVENT_URL)
        await page.wait_for_timeout(5000)
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

def read_last_alert():
    doc = doc.get()
    if doc.exists:
        return doc.to_dict().get("last_price", 0.0)
    return 0.0

def save_last_alert(price):
    doc.set({"last_price": price})
    
async def check_prices():
    prices = await fetch_prices()
    if not prices:
        print("No prices found.")
        return
    
    lowest_price = float(min(prices))
    print(f"Lowest price found: ${lowest_price}")
    
    last_alerted = read_last_alert()
    print(f"Last alerted price: ${last_alerted}")
   
    if ((lowest_price <= TARGET_PRICE) and (lowest_price != last_alerted)):
        send_discord_alert(lowest_price)
        save_last_alert(lowest_price)
        print(f"Alert sent for ${lowest_price}!")
    else:
        print("No new alert needed.")

if __name__ == "__main__":
    asyncio.run(check_prices())