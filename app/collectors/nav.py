import json
import requests
import trafilatura

from tqdm import tqdm
from zoneinfo import ZoneInfo
from pathlib import Path
from email.utils import format_datetime
from datetime import datetime, UTC, timedelta

from app.config.settings import NAV_TOKEN
from app.collectors.base import BaseCollector
from app.models import JobPosting
from app.matching.title_filter import TitleFilter

STATE_FILE = Path('data/feed_state.json')

def load_feed_state():

    if not STATE_FILE.exists():
        return {
            'last_modified': None,
            'etag': None
        }

    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def save_feed_state(
    last_modified,
    etag
):
    with open(STATE_FILE, 'w') as f:
        json.dump(
            {
                'last_modified': last_modified,
                'etag': etag
            },
            f,
            indent=4
        )

state = load_feed_state()

class NavCollector(BaseCollector):

    def collect(self):

        data = self._download_feed()

        jobs = self._parse_jobs(data)
        
        return jobs

    def _download_feed(self):

        headers = {
            'Authorization': f'Bearer {NAV_TOKEN}',
            'Accept': 'application/json'
        }
        
        last_modified = state.get('last_modified')
        if last_modified is not None:
            headers['If-Modified-Since'] = last_modified
        else:
            two_weeks = datetime.now(ZoneInfo('Europe/Oslo')) - timedelta(days=14)
            headers['If-Modified-Since'] = format_datetime(
                two_weeks.astimezone(UTC),
                usegmt=True
            )
        etag = state.get('etag')
        if etag is not None:
            headers['If-None-Match'] = etag
            
        feed_page = "/api/v1/feed"

        all_items = []

        last_modified = None
        etag = None
        
        page_count = 0

        while feed_page:

            page_count += 1

            print(
                f"Downloading page {page_count}: " +
                f"{feed_page}"
            )

            print(last_modified)
        
            response = requests.get(
                'https://pam-stilling-feed.nav.no' + feed_page,
                headers=headers
            )
            if response.status_code == 304:
                return []

            response.raise_for_status()

            data = response.json()
            all_items.extend(data['items'])

            feed_page = data.get('next_url')

            last_modified = response.headers.get(
                "Last-Modified"
            )

            etag = response.headers.get(
                "ETag"
            )


        save_feed_state(
            last_modified,
            etag
        )

        return all_items

    def _parse_jobs(self, all_items):
        
        jobs = []

        tfilter = TitleFilter()
        
        for item in tqdm(all_items, desc='Parsing jobs'):
            
            feed_entry = item['_feed_entry']

            if feed_entry['status'] != 'ACTIVE':
                continue


            if not tfilter.matches(item['title']):
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

        return (job_entry.get('ad_content', {}).get('description'))

    def _fetch_job_details(self, relative_url):

        url = f'https://pam-stilling-feed.nav.no{relative_url}'

        try:
            response = requests.get(
                url,
                headers={
                    'Authorization': f'Bearer {NAV_TOKEN}'
                },
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Failed: {url}")
            print(e)
            return None

        return response.json()




