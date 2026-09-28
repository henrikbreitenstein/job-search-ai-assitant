import json
import requests

from app.config.settings import NAV_TOKEN

response = requests.get(
    'https://pam-stilling-feed.nav.no/api/v1/feedentry/ac1d9b5c-2c4c-4e12-9778-32b36a599682',
    headers={
    'Authorization': f'Bearer {NAV_TOKEN}'
    }
)


#response = requests.get(
#            'https://pam-stilling-feed.nav.no/api/v1/feed',
#            headers={
#                'If-Modified-Since' : 'Fri, 25 Sep 2026 00:00:00 +0200',
#                'Authorization': f'Bearer {NAV_TOKEN}'
#                }
#            )

response.raise_for_status()

print(response.json())
