from app.database.repository import JobRepository

def main():
    repository = JobRepository()

    jobs = repository.get_unreported_above_fit_score(
        threshold=70
    )

    reported_ids = []
    base_link="https://arbeidsplassen.nav.no/stillinger/stilling/"

    for job in jobs:

        print(40*'-')
        print(job.title, ' ', job.fit_score)
        print(40*'-')
        print(base_link + job.url.split('/')[-1])
        reported_ids.append(job.id)

    for job_id in reported_ids:
        repository.mark_reported(
            job_id
        )
