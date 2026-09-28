from app.collectors.fake_nav import FakeNavCollector
from app.processing.skill_extractor import SkillExtractor
from app.matching.matching import Matcher
from app.llm.analyzer import JobAnalyzer
from app.llm.profile_builder import build_profile
from app.processing.skill_extractor import SKILLS

collector = FakeNavCollector()
matcher = Matcher(SKILLS)
analyzer = JobAnalyzer()
extractor = SkillExtractor()

jobs = collector.collect()
PROFILE = build_profile()

for job in jobs:

    skills = extractor.extract(
        job.description
    )

    score = matcher.score(
        job,
        skills
    )

    if score < 0.4:
        continue

    analysis = analyzer.analyze(
        PROFILE,
        job
    )

    print(job.title)
    print(analysis)

