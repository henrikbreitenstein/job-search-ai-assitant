from app.collectors.fake_nav import FakeNavCollector
from app.processing.skill_extractor import SkillExtractor
from app.matching.matching import Matcher
from app.processing.skill_extractor import SKILLS


collector = FakeNavCollector()
extractor = SkillExtractor()
matcher = Matcher(SKILLS)

jobs = collector.collect()

for job in jobs:

    job_skills = extractor.extract(
        job.description
    )

    score = matcher.score(
        job,
        job_skills
    )

    print("=" * 50)
    print(f"Title: {job.title}")
    print(f"Company: {job.company}")
    print(f"Skills: {job_skills}")
    print(f"Score: {score:.2f}")
