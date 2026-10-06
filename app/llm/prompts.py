
def build_job_prompt(
    profile,
    job
):

    return f'''

Candidate profile:

{profile}

Job title:
{job.title}

Company:
{job.company}

Description:
{job.description}

Evaluate how well this candidate matches the role.

Return JSON only, in the this format:

{{
    "fit_score": 0-100,
    "seniority": "The seniority level of the role [Low, Mid, High]",
    "years_experience": Optinal[int] number of years of experience,
    "analysis": "Why the score is what it is.",
    "strengths": [
        "Python",
        "Machine Learning"
    ],
    "gaps": [
        "Azure", "Excel"
    ]
}}
    '''
