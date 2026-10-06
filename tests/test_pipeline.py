from app.collectors.fake_nav import FakeNavCollector
from app.database import repository
from app.processing.skill_extractor import SkillExtractor
from app.matching.matching import Matcher
from app.llm.analyzer import JobAnalyzer
from app.database.repository import JobRepository
from app.llm.profile_builder import build_profile
from app.processing.skill_extractor import SKILLS

collector = FakeNavCollector()
matcher = Matcher(SKILLS)
analyzer = JobAnalyzer()
extractor = SkillExtractor()
repository = JobRepository()

jobs = collector.collect()
PROFILE = build_profile()

jobs = collector.collect()

for job in jobs:

    repository.insert(job)

for job in repository.get_unprocessed():

    skills = extractor.extract(
        job.description
    )

    score = matcher.score(
        job,
        skills
    )

    job.skill_score = score

    if score < 0.4:
        print('Not fit')
        continue

    analysis = analyzer.analyze(
        PROFILE,
        job
    )

    job.analysis = analysis
    job.processed = True

    print(job.title)
    print(analysis)

