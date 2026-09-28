from app.collectors.nav import NavCollector
from app.database.repository import JobRepository

collector = NavCollector()

jobs = collector.collect()

for job in jobs:
    JobRepository().insert(job)
