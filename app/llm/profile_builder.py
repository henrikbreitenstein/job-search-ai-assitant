from app.config.profile import PROFILE


def build_profile():

    return f"""
Education:
{", ".join(PROFILE["education"])}

Skills:
{", ".join(PROFILE["skills"])}

Preferred roles:
{", ".join(PROFILE["preferred_roles"])}

Experience level:
{PROFILE["experience_level"]}
"""
