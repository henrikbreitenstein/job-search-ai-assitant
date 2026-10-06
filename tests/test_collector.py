from app.collectors.nav import NavCollector

collector = NavCollector()

jobs = collector.collect()

for job in jobs:

    print(job)
