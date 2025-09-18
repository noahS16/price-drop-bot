from datetime import datetime
import requests
import os
from dotenv import load_dotenv
import headers
import pprint

load_dotenv()

# Config
EVENT_URL = os.environ.get("EVENT_URL")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")
TARGET_PRICE = float(os.environ.get("TARGET_PRICE", "300"))
    
def send_discord_alert(message: str):
    try:
        resp = requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=100)
        if resp.status_code != 204:
            print(f"Discord webhook failed: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Error sending Discord alert: {e}")

def get_lowest_price():
    RESPONSE = headers.RESPONSE
    print("Response code: ", RESPONSE.status_code)
    data = RESPONSE.json()
    tickets = data.get('facets', {})
    print("Length of facets: ", len(tickets))
    #pprint.pprint(tickets)
    prices = []
    for ticket in tickets:
        prices.append(ticket.get('totalPriceRange', {})[0].get('min', 0))
    print("Prices: ", prices)
    return min(prices)

def check_prices():
    cheapest = get_lowest_price()
    print("Cheapest: ", cheapest)
    if cheapest <= TARGET_PRICE or cheapest <=200.0:
        message = f"🎸 Ticket available for **${cheapest}**!\n{os.environ.get('EVENT_URL')}"
        send_discord_alert(message)


def check_time():
    current_time = datetime.now()
    target_hour = 19  # 10 PM
    if current_time.hour == 19 or current_time.hour == 10:
        lowest_price = get_lowest_price()
        send_discord_alert(f"🤑 The lowest ticket price rn is **${lowest_price}**\n{EVENT_URL}")


if __name__ == "__main__":
    check_prices()
    check_time()
