from app.database import repository
from app.database.repository import JobRepository
from app.processing.skill_extractor import SkillExtractor
from app.matching.matching import Matcher
from app.llm.analyzer import JobAnalyzer
from app.llm.profile_builder import build_profile

repository = JobRepository()
extractor = SkillExtractor()
matcher = Matcher()
analyzer = JobAnalyzer()

PROFILE = build_profile()

jobs = repository.get_unprocessed()

for job in jobs:

    skills = extractor.extract(job)
    score = matcher.score(job, skills)

    repository.update_score(
        job.id,
        score
    )

    if score < 0.4:
        repository.mark_processed(
            job.id
        )
        continue

    result = analyzer.analyze(
        PROFILE,
        job
    )

    repository.update_analysis(
        job.id,
        result
    )

    repository.mark_processed(
        job.id
    )
