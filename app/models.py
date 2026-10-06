from dataclasses import dataclass
from typing import Optional

@dataclass
class JobPosting:
    title: str
    company: str
    location: str
    url: str
    description: str
    
    id: Optional[int] = None

    skill_score: float = 0.0
    fit_score: float = 0.0

    seniority: Optional[str] = None
    years_experience: Optional[int] = None

    strengths: Optional[str] = None
    gaps: Optional[str] = None

    analysis: Optional[str] = None

    processed: bool = False
