from app.processing.skill_extractor import SkillExtractor

descriptor = """
We are looking for a Data Scientist with experience
in Python, SQL, Docker and Machine Learning.
Experience with Azure is a plus.
"""

extractor = SkillExtractor()

skills = extractor.extract(descriptor)

print(skills)
