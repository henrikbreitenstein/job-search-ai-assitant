import re

WORK_EXPERIENCE_PATTERNS = [
    r"(\d+)\+?\s*years? of professional experience",
    r"(\d+)\+?\s*years? of relevant experience",
    r"(\d+)\+?\s*years? of work experience",
    r"minimum\s*(\d+)\s*years? experience",

    r"(\d+)\+?\s*års relevant erfaring",
    r"(\d+)\+?\s*års arbeidserfaring",
    r"minimum\s*(\d+)\s*års erfaring",
]


SENIOR_TITLE_KEYWORDS = {
    "senior",
    "lead",
    "principal",
    "staff",
    "head of",
    "director",
    "chief"
}


class Matcher:

    def __init__(self, profile_skills):

        self.profile_skills = set(profile_skills)

    def is_senior_title(self, title):

        title = title.lower()

        return any(
            keyword in title
            for keyword in SENIOR_TITLE_KEYWORDS
        )

    def score(self, job, job_skills):

        if self.is_senior_title(job.title):
            return 0.0

        job_skills = set(job_skills)

        if not job_skills:
            return 0.0

        matches = self.profile_skills & job_skills
        score = len(matches) / len(job_skills)

        years_required = self.extract_work_experience(
            job.description
        )

        if years_required >= 5:
            score *= 0.5

        return score

    def extract_work_experience(self, text):

        text = text.lower()

        years = []

        for pattern in WORK_EXPERIENCE_PATTERNS:

            matches = re.findall(pattern, text)

            years.extend(
                int(match)
                for match in matches
            )
        
        return max(years, default=0)
