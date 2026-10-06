from app.collectors.nav import NavCollector
from app.database.repository import JobRepository

def main():
    collector = NavCollector()

    jobs = collector.collect()

    for job in jobs:
        JobRepository().insert(job)


if __name__ == "__main__":
    main()
