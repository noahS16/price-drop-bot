import requests
import pprint

cookies = {
    'tk-u': 'ZmZkYzQxYzQtZThkMy00ZWU4LTg1ODItMzczOGRlNmIxM2Iw',
    'tk-api-email': 'bm9haHNhZW56MDE2QGdtYWlsLmNvbQ',
    'tk-api-key': 'WyJOZXdKakxEVkdTQmpYcGczczIzVncySkd4SHBuTEFBdiJd',
    'tk-api-apps': 'W3sibmFtZSI6Im5vYWhzMTYtQXBwIiwiY3JlYXRlZCI6IjIwMjUtMDgtMjYgMDc6NTQgQU0iLCJrZXkiOiJOZXdKakxEVkdTQmpYcGczczIzVncySkd4SHBuTEFBdiJ9XQ',
    'tk-user-roles': 'WyJhdXRoZW50aWNhdGVkIHVzZXIiXQ',
    'SSESSba67f03972f55553598b0a8abebb2c0d': 'cJMRjFHnOH6z4-nd4pPAI4tZffBO9zoOIp0jjbn11JU',
    'BID': 'AxHYREcKQjdn3wOQsx33ubFUz1PRQmDj9jksrpgR6Wlvyvsf9W2ZYzybkFV1tKShMNBK7t59j0WYIWqg',
    'LANGUAGE': 'en-us',
    'eps_sid': '49fee25751fa78a9168e5514092542974ed4bca4',
    '_gcl_au': '1.1.330106136.1756235301',
    '_au_1d': 'AU1D0200001756235302WV0ZP6R7VK0E',
    '_scid': 'tXoqavR-z1qiqV_lnSGujXiP5urodBaM',
    '_fbp': 'fb.1.1756235302101.73718270865867957',
    '_tt_enable_cookie': '1',
    '_ttp': '01K3KWG185MJBF5C1FDDXKS3BK_.tt.1',
    '_cs_c': '0',
    'OptanonGroups': ',C0001,C0003,C0002,C0004,',
    '__qca': 'P1-2a4244f0-761f-4c44-a95d-52360d37e762',
    'mt.v': '2.1602451668.1756235302538',
    '_gcl_dc': 'GCL.1756235311.CjwKCAjwtrXFBhBiEiwAEKen1xDj3lGNXbuWGpjT-Rdkzarc58onHtnLcJtx_a4awx0fl2cne35ovxoCNJAQAvD_BwE',
    '_pin_unauth': 'dWlkPVptSXlZVGxoTXpRdE1XTmtaUzAwTmpNd0xXSTJNMll0TkRVMll6QmtaREZsWlRobQ',
    '_gcl_gs': '2.1.k1$i1756272004$u27656889',
    '_ga_c': 'SEM_TMMCONCERTS_ggl_22878028473_184414426715_the strokes tickets',
    '_ga_otc': 'SEM_TMMCONCERTS_ggl_22878028473_184414426715_the strokes tickets',
    'XDA': '{"cfc":"yes","tmm_sem":"K8vZ9171UUf,,KZFzniwnSyZfZ7v7nJ","nac_sem":"","tms_sem":""}',
    '_gac_UA-60025178-2': '1.1756272007.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE',
    'ken_gclid': 'CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE',
    'ken_gbraid': '0AAAAAD_KsMLS--U6QUrtcB2yatx9fBtMq',
    '_gcl_aw': 'GCL.1756272008.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE',
    '_gac_UA-60025178-1': '1.1756272009.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE',
    '_ga_KZKCRXEDNX': 'GS2.2.s1756881735$o2$g0$t1756881735$j60$l0$h0',
    'tmpt': '0:68b1fa36ce000000:1758138972:d6e6e0a0:7e19d610b050cac0f118fcce1fb3f075:e272709248de1136a4de7471b0b7064a780f459fe24e8b252a873165c289d5b9',
    'SID': 'D-XvIwYJGZu59GiEtAP07bsNdUMxvdx_HDtCC_yfMDaWsHVRLUNQydwbON1nIHGEKkiIC3D94Uw5Di4I',
    'mt.pc': '2.1',
    'TMUO': 'west_8oKONkCTWkRHzNIOhxftigOwUSn8em1xKWwnxeyJBtg=',
    'mt.g.2f013145': '2.1602451668.1756235302538',
    '_gid': 'GA1.2.646334113.1758138974',
    'TM_PIXEL': '{"_dvs":"0:mfoejusp:tlrWaFZX2xZNO0Ky37jknM9FNYbg5A7g","_dvp":"0:mesx5jww:9cJ70lnmQ2rInbHjZfraCOj3n5ADZ4rZ"}',
    '_ScCbts': '%5B%5D',
    '_sctr': '1%7C1758088800000',
    'ttcsid_D108SKRC77U8IVAA9SP0': '1758141093858::8N0-0jE3GTcxVYju3lsL.11.1758141094769.0',
    '_ga': 'GA1.2.1563616872.1756194722',
    '_scid_r': 'z_oqavR-z1qiqV_lnSGujXiP5urodBaMWBm7-g',
    '_rdt_uuid': '1756235302047.9332f046-eaf5-4f94-bba0-e4422be9ecb3',
    '_uetsid': '5e084d20940011f081dc0d6f8b6bff5f|1046lzj|2|fze|0|2086',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Sep+17+2025+14%3A31%3A35+GMT-0600+(Mountain+Daylight+Time)&version=202506.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5992f3d8-75d7-451e-a740-4d93e373154e&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'ttcsid': '1758141093859::fJUCSPqAFvbUaUiUUf3g.11.1758141095736.0',
    'ttcsid_CDBG7BRC77U0N3GC39K0': '1758141095563::8tnxYjwLcTYFCgMJ94y-.11.1758141095862.0',
    'ttcsid_CFSIOARC77UADV8CV30G': '1758141095649::fxyhoej11L84TKQtwYOa.11.1758141095911.0',
    'ttcsid_CFSIKRBC77UBIS8PMC8G': '1758141095650::ISPu6T-EQCHLgE5qYUIr.11.1758141095911.0',
    'ttcsid_CFSINGRC77UBIS8PMC9G': '1758141095651::j0jtTO56KcH6jpxFSHQz.11.1758141095911.0',
    'ttcsid_CFSIOR3C77U5NAK3O40G': '1758141095652::5YKicDcciBt7qnl3RcEz.11.1758141095911.0',
    'ttcsid_CFSIQIRC77U92D2F42J0': '1758141095652::Zgm6zpSqZLHu8VeO2M5G.11.1758141095911.0',
    '_uetvid': '08d435a082b011f0813683fabae4d6da|1diupua|1758141096059|1|1|bat.bing.com/p/insights/c/o',
    'ttcsid_CK1728RC77U2Q32CJ8IG': '1758141095735::Ryjt01igme3Fgm-x1NC5.11.1758141096078.0',
    '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Name%22%2C%22TM_US%3A%20CCP%20EDP%3A%20RS%3A%20Offsale%22%5D%2C%222%22%3A%5B%22Page%20Type%22%2C%22CCP%20EDP%3A%20Offsale%22%5D%2C%223%22%3A%5B%22Modules%20Available%22%2C%22EDP_RseAllinPricing_USNeedtoKnowCal%22%5D%2C%224%22%3A%5B%22Platform%22%2C%22ccp-edp%22%5D%2C%225%22%3A%5B%22Login%20Status%22%2C%22Not%20Logged%20In%22%5D%2C%226%22%3A%5B%22Major%20Category%22%2C%22Music%22%5D%2C%227%22%3A%5B%22Minor%20Category%22%2C%22Rock%22%5D%2C%228%22%3A%5B%22Artist%20ID%22%2C%22807068%22%5D%2C%229%22%3A%5B%22Artist%20Name%22%2C%22The%20Strokes%22%5D%2C%2210%22%3A%5B%22Venue%20ID%22%2C%2298429%22%5D%2C%2211%22%3A%5B%22Event%20ID%22%2C%220C0062FFBD8C2B60%22%5D%2C%2212%22%3A%5B%22Event%20Date%22%2C%2210%2F1%2F2025%22%5D%2C%2213%22%3A%5B%22EDP%20Page%20Type%22%2C%22CCP%20EDP%3A%20SIM%22%5D%2C%2214%22%3A%5B%22Event%20Type%22%2C%22STANDARD%22%5D%7D',
    '_cs_id': 'cd5e2185-c1c1-a0ea-ce0e-6da683f21970.1756235302.52.1758141096.1758141080.1752251019.1790399302238.1.x',
    '_cs_s': '3.0.1.9.1758142926197',
    '_pn': 'eyJzdWIiOnsidWRyIjowLCJpZCI6IjR6SW5jV3VBaW9tTWlTNTFUcjJoa1QxWXpBMDZnN05mIiwic3MiOjEsImRzZSI6MTc1ODc0NTkzNDU1Mn0sImx1YSI6MTc1ODE0MTEzNDU1Mn0',
    '_ga_C1T806G4DF': 'GS2.1.s1758141090$o17$g1$t1758141155$j60$l0$h0',
    '_ga_H1KKSGW33X': 'GS2.1.s1758141090$o17$g1$t1758141155$j60$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-modified-since': 'Wed, 17 Sep 2025 19:54:08 GMT',
    'if-none-match': 'W/"05aa771ee25e2e5c40cc6bd49688ac4d0"',
    'origin': 'https://www.ticketmaster.com',
    'priority': 'u=1, i',
    'referer': 'https://www.ticketmaster.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'tmps-correlation-id': 'c1f95b05-65b3-41a5-bf53-6920b7413303',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': 'tk-u=ZmZkYzQxYzQtZThkMy00ZWU4LTg1ODItMzczOGRlNmIxM2Iw; tk-api-email=bm9haHNhZW56MDE2QGdtYWlsLmNvbQ; tk-api-key=WyJOZXdKakxEVkdTQmpYcGczczIzVncySkd4SHBuTEFBdiJd; tk-api-apps=W3sibmFtZSI6Im5vYWhzMTYtQXBwIiwiY3JlYXRlZCI6IjIwMjUtMDgtMjYgMDc6NTQgQU0iLCJrZXkiOiJOZXdKakxEVkdTQmpYcGczczIzVncySkd4SHBuTEFBdiJ9XQ; tk-user-roles=WyJhdXRoZW50aWNhdGVkIHVzZXIiXQ; SSESSba67f03972f55553598b0a8abebb2c0d=cJMRjFHnOH6z4-nd4pPAI4tZffBO9zoOIp0jjbn11JU; BID=AxHYREcKQjdn3wOQsx33ubFUz1PRQmDj9jksrpgR6Wlvyvsf9W2ZYzybkFV1tKShMNBK7t59j0WYIWqg; LANGUAGE=en-us; eps_sid=49fee25751fa78a9168e5514092542974ed4bca4; _gcl_au=1.1.330106136.1756235301; _au_1d=AU1D0200001756235302WV0ZP6R7VK0E; _scid=tXoqavR-z1qiqV_lnSGujXiP5urodBaM; _fbp=fb.1.1756235302101.73718270865867957; _tt_enable_cookie=1; _ttp=01K3KWG185MJBF5C1FDDXKS3BK_.tt.1; _cs_c=0; OptanonGroups=,C0001,C0003,C0002,C0004,; __qca=P1-2a4244f0-761f-4c44-a95d-52360d37e762; mt.v=2.1602451668.1756235302538; _gcl_dc=GCL.1756235311.CjwKCAjwtrXFBhBiEiwAEKen1xDj3lGNXbuWGpjT-Rdkzarc58onHtnLcJtx_a4awx0fl2cne35ovxoCNJAQAvD_BwE; _pin_unauth=dWlkPVptSXlZVGxoTXpRdE1XTmtaUzAwTmpNd0xXSTJNMll0TkRVMll6QmtaREZsWlRobQ; _gcl_gs=2.1.k1$i1756272004$u27656889; _ga_c=SEM_TMMCONCERTS_ggl_22878028473_184414426715_the strokes tickets; _ga_otc=SEM_TMMCONCERTS_ggl_22878028473_184414426715_the strokes tickets; XDA={"cfc":"yes","tmm_sem":"K8vZ9171UUf,,KZFzniwnSyZfZ7v7nJ","nac_sem":"","tms_sem":""}; _gac_UA-60025178-2=1.1756272007.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE; ken_gclid=CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE; ken_gbraid=0AAAAAD_KsMLS--U6QUrtcB2yatx9fBtMq; _gcl_aw=GCL.1756272008.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE; _gac_UA-60025178-1=1.1756272009.CjwKCAjwtrXFBhBiEiwAEKen10p47f9a4_vc8LU9nhXA2xM1Ef01bT8jMRNTelZAGtqSYpDTaI6JxRoCdzwQAvD_BwE; _ga_KZKCRXEDNX=GS2.2.s1756881735$o2$g0$t1756881735$j60$l0$h0; tmpt=0:68b1fa36ce000000:1758138972:d6e6e0a0:7e19d610b050cac0f118fcce1fb3f075:e272709248de1136a4de7471b0b7064a780f459fe24e8b252a873165c289d5b9; SID=D-XvIwYJGZu59GiEtAP07bsNdUMxvdx_HDtCC_yfMDaWsHVRLUNQydwbON1nIHGEKkiIC3D94Uw5Di4I; mt.pc=2.1; TMUO=west_8oKONkCTWkRHzNIOhxftigOwUSn8em1xKWwnxeyJBtg=; mt.g.2f013145=2.1602451668.1756235302538; _gid=GA1.2.646334113.1758138974; TM_PIXEL={"_dvs":"0:mfoejusp:tlrWaFZX2xZNO0Ky37jknM9FNYbg5A7g","_dvp":"0:mesx5jww:9cJ70lnmQ2rInbHjZfraCOj3n5ADZ4rZ"}; _ScCbts=%5B%5D; _sctr=1%7C1758088800000; ttcsid_D108SKRC77U8IVAA9SP0=1758141093858::8N0-0jE3GTcxVYju3lsL.11.1758141094769.0; _ga=GA1.2.1563616872.1756194722; _scid_r=z_oqavR-z1qiqV_lnSGujXiP5urodBaMWBm7-g; _rdt_uuid=1756235302047.9332f046-eaf5-4f94-bba0-e4422be9ecb3; _uetsid=5e084d20940011f081dc0d6f8b6bff5f|1046lzj|2|fze|0|2086; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+17+2025+14%3A31%3A35+GMT-0600+(Mountain+Daylight+Time)&version=202506.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5992f3d8-75d7-451e-a740-4d93e373154e&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; ttcsid=1758141093859::fJUCSPqAFvbUaUiUUf3g.11.1758141095736.0; ttcsid_CDBG7BRC77U0N3GC39K0=1758141095563::8tnxYjwLcTYFCgMJ94y-.11.1758141095862.0; ttcsid_CFSIOARC77UADV8CV30G=1758141095649::fxyhoej11L84TKQtwYOa.11.1758141095911.0; ttcsid_CFSIKRBC77UBIS8PMC8G=1758141095650::ISPu6T-EQCHLgE5qYUIr.11.1758141095911.0; ttcsid_CFSINGRC77UBIS8PMC9G=1758141095651::j0jtTO56KcH6jpxFSHQz.11.1758141095911.0; ttcsid_CFSIOR3C77U5NAK3O40G=1758141095652::5YKicDcciBt7qnl3RcEz.11.1758141095911.0; ttcsid_CFSIQIRC77U92D2F42J0=1758141095652::Zgm6zpSqZLHu8VeO2M5G.11.1758141095911.0; _uetvid=08d435a082b011f0813683fabae4d6da|1diupua|1758141096059|1|1|bat.bing.com/p/insights/c/o; ttcsid_CK1728RC77U2Q32CJ8IG=1758141095735::Ryjt01igme3Fgm-x1NC5.11.1758141096078.0; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22TM_US%3A%20CCP%20EDP%3A%20RS%3A%20Offsale%22%5D%2C%222%22%3A%5B%22Page%20Type%22%2C%22CCP%20EDP%3A%20Offsale%22%5D%2C%223%22%3A%5B%22Modules%20Available%22%2C%22EDP_RseAllinPricing_USNeedtoKnowCal%22%5D%2C%224%22%3A%5B%22Platform%22%2C%22ccp-edp%22%5D%2C%225%22%3A%5B%22Login%20Status%22%2C%22Not%20Logged%20In%22%5D%2C%226%22%3A%5B%22Major%20Category%22%2C%22Music%22%5D%2C%227%22%3A%5B%22Minor%20Category%22%2C%22Rock%22%5D%2C%228%22%3A%5B%22Artist%20ID%22%2C%22807068%22%5D%2C%229%22%3A%5B%22Artist%20Name%22%2C%22The%20Strokes%22%5D%2C%2210%22%3A%5B%22Venue%20ID%22%2C%2298429%22%5D%2C%2211%22%3A%5B%22Event%20ID%22%2C%220C0062FFBD8C2B60%22%5D%2C%2212%22%3A%5B%22Event%20Date%22%2C%2210%2F1%2F2025%22%5D%2C%2213%22%3A%5B%22EDP%20Page%20Type%22%2C%22CCP%20EDP%3A%20SIM%22%5D%2C%2214%22%3A%5B%22Event%20Type%22%2C%22STANDARD%22%5D%7D; _cs_id=cd5e2185-c1c1-a0ea-ce0e-6da683f21970.1756235302.52.1758141096.1758141080.1752251019.1790399302238.1.x; _cs_s=3.0.1.9.1758142926197; _pn=eyJzdWIiOnsidWRyIjowLCJpZCI6IjR6SW5jV3VBaW9tTWlTNTFUcjJoa1QxWXpBMDZnN05mIiwic3MiOjEsImRzZSI6MTc1ODc0NTkzNDU1Mn0sImx1YSI6MTc1ODE0MTEzNDU1Mn0; _ga_C1T806G4DF=GS2.1.s1758141090$o17$g1$t1758141155$j60$l0$h0; _ga_H1KKSGW33X=GS2.1.s1758141090$o17$g1$t1758141155$j60$l0$h0',
}

params = {
    'show': 'totalpricerange',
    'by': 'offers',
    'q': 'available',
    'apikey': 'b462oi7fic6pehcdkzony5bxhe',
    'apisecret': 'pquzpfrfz7zd2ylvtz3w5dtyse',
    'resaleChannelId': 'internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us',
}

RESPONSE = requests.get(
    'https://offeradapter.ticketmaster.com/api/ismds/event/0C0062FFBD8C2B60/facets',
    params=params,
    cookies=cookies,
    headers=headers,
)


# print(RESPONSE.status_code)
# data = RESPONSE.json()
# tickets = data.get('facets', {})
# print("Length of facets: ", len(tickets))
# pprint.pprint(tickets)
# prices = []
# for ticket in tickets:
#     prices.append(ticket.get('totalPriceRange', {})[0].get('min', 0))
# print("Prices: ", prices)
# cheapest = min(prices)
# print("Cheapest: ", cheapest)