import re

from app.processing.skill_extractor import SENIOR_TITLE_KEYWORDS

TITLE_KEYWORDS = {
    "data scientist",
    "data engineer",
    "data analyst",
    "analyst",
    "analytiker",
    "dataingeniør",
    "maskinlæring",
    "machine learning",
    "ai",
    "ki",
    "ai engineer",
    "ai developer",
    "utvikler",
    "datautvikler",
    "business intelligence",
    "bi",
    "nlp",
    "computer vision",
    "mlops"
}
class TitleFilter:

    def matches(self, title):

        title = title.lower()

        for senior_word in SENIOR_TITLE_KEYWORDS:

            if senior_word in title:
                return False

        for keyword in TITLE_KEYWORDS:

            if keyword in title:
                return True

        return False
