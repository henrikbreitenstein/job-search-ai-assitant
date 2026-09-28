
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

Return JSON only:

{{
    "fit_score": 0-10,
    "matching_skills": [],
    "missing_skills": [],
    "reasoning": ""
}}
    '''
