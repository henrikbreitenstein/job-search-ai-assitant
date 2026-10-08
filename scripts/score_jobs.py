from app.database import repository
from tqdm import tqdm
from app.database.repository import JobRepository
from app.processing.skill_extractor import SkillExtractor
from app.matching.matching import Matcher
from app.llm.analyzer import JobAnalyzer
from app.llm.profile_builder import build_profile
from app.processing.skill_extractor import SKILLS

def main():
    repository = JobRepository()
    extractor = SkillExtractor()
    matcher = Matcher(SKILLS)
    analyzer = JobAnalyzer()

    PROFILE = build_profile()

    jobs = repository.get_unprocessed()

    for job in tqdm(jobs, desc='Scoring'):

        skills = extractor.extract(job.description)
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
