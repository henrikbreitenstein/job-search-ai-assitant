import json
import requests
import trafilatura

from zoneinfo import ZoneInfo
from email.utils import format_datetime
from datetime import datetime, UTC, timedelta

from app.config.settings import NAV_TOKEN
from app.collectors.base import BaseCollector
from app.models import JobPosting

class NavCollector(BaseCollector):

    def collect(self):

        data = self._download_feed()

        jobs = self._parse_jobs(data)
        
        return jobs

    def _download_feed(self):

        yesterday = datetime.now(ZoneInfo('Europe/Oslo')) - timedelta(days=1)

        if_modified_since = format_datetime(
            yesterday.astimezone(UTC),
            usegmt=True
        )
        
        response = requests.get(
            'https://pam-stilling-feed.nav.no/api/v1/feed',
            headers={
                'If-Modified-Since' : if_modified_since,
                'Authorization': f'Bearer {NAV_TOKEN}'
            }
        )

        response.raise_for_status()

        return response.json()

    def _parse_jobs(self, data):
        
        jobs = []
        
        for item in data['items']:
            
            feed_entry = item['_feed_entry']

            if feed_entry['status'] != 'ACTIVE':
                continue

            description = self._check_if_active(item['url'])

            if not description:
                continue

            job = JobPosting(
                title=item['title'],
                company=feed_entry['businessName'],
                location=feed_entry['municipal'],
                url=item['url'],
                description=description
            )

            jobs.append(job)

        return jobs

    def _check_if_active(self, entry_url):

        nav_base_url = 'https://pam-stilling-feed.nav.no'
        job_url = nav_base_url + entry_url

        response = requests.get(
            job_url,
            headers={
                'Authorization': f'Bearer {NAV_TOKEN}'
            }
        )

        response.raise_for_status()
        job_entry = response.json()

        if job_entry['status'] != 'ACTIVE':
            return False

        try:
            return job_entry['description']
        except:
            return False

    def _fetch_job_details(self, relative_url):

        url = f'https://pam-stilling-feed.nav.no{relative_url}'

        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {NAV_TOKEN}'
            }
        )
        response.raise_for_status()

        return response.json()



data = NavCollector()._download_feed()['items']
count = 0
for item in data:
    if item['_feed_entry']['status'] == 'ACTIVE':
        count += 1
print(count)


