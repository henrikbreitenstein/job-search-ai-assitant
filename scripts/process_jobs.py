from app.database import repository
from app.database.repository import JobRepository
from app.processing.skill_extractor import SkillExtractor

repository = JobRepository()
extractor = SkillExtractor()

jobs = repository.get_unprocessed()

for job in jobs:

    skills = extractor.extract(job)

    print(job.title)
    print(skills)
    print()

    repository.mark_processed(job.id)
