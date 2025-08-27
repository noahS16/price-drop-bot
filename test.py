import requests

url = "https://offeradapter.ticketmaster.com/api/ismds/event/0C0062FFBD8C2B60/facets"
params = {
    "show": "totalpricerange",
    "by": "offers",
    "q": "available",
    "apikey": "b462oi7fic6pehcdkzony5bxhe",
    "apisecret": "pquzpfrfz7zd2ylvtz3w5dtyse",
    "resaleChannelId": "internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Origin": "https://www.ticketmaster.com",
    "Referer": "https://www.ticketmaster.com/",
    "Cookie": "_gid=GA1.2.785721488.1756194722; tk-u=ZmZkYzQxYzQtZThkMy00ZWU4LTg1ODItMzczOGRlNmIxM2Iw; ...",  # <-- paste full cookie string here
    "tmps-correlation-id": "9ed9673d-f702-414c-a785-26de3411d1ca",
}

resp = requests.get(url, params=params, headers=headers)

print(resp.status_code)
print(resp.text)  # or resp.json() if it's JSON