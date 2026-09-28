import json

from app.llm.client import LLMClient
from app.llm.prompts import build_job_prompt

class JobAnalyzer:

    def __init__(self):

        self.client = LLMClient()

    def analyze(self, profile, job):

        prompt = build_job_prompt(
            profile,
            job
        )

        response = self.client.ask(
            prompt
        )

        return json.loads(response)

