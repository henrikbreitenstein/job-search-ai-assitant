from app.collectors.base import BaseCollector
from app.models import JobPosting

class FakeNavCollector(BaseCollector):

    def collect(self):

        return [
            JobPosting(
                title="Data Scientist",
                company="Statnett",
                location="Oslo",
                url="https://example.com/job1",
                description="""
                We are looking for a Data Scientist.

                Requirements:
                - Python
                - SQL
                - Pandas
                - Machine Learning
                - Statistical Modeling

                Nice to have:
                - Azure
                - Docker
                """
            ),

            JobPosting(
                title="AI Engineer",
                company="Gjensidige",
                location="Oslo",
                url="https://example.com/job2",
                description="""
                We are looking for an AI Engineer.

                Requirements:
                - Python
                - PyTorch
                - TensorFlow
                - Generative AI
                - RAG

                Nice to have:
                - Kubernetes
                - Azure
                """
            ),

            JobPosting(
                title="Data Analyst",
                company="Storebrand",
                location="Oslo",
                url="https://example.com/job3",
                description="""
                We are looking for a Data Analyst.

                Requirements:
                - SQL
                - Power BI
                - Excel
                - Data Analysis

                Nice to have:
                - Python
                """
            ),

            JobPosting(
                title="Warehouse Worker",
                company="Asko",
                location="Oslo",
                url="https://example.com/job4",
                description="""
                Warehouse worker wanted.

                Requirements:
                - Forklift License
                - Physical work
                - Teamwork

                Nice to have:
                - Logistics experience
                """
            ),

            JobPosting(
                title="Machine Learning Engineer",
                company="Schibsted",
                location="Oslo",
                url="https://example.com/job5",
                description="""
                Machine Learning Engineer.

                Requirements:
                - Python
                - Machine Learning
                - PyTorch
                - Docker
                - SQL

                Nice to have:
                - AWS
                - Kubernetes
                """
            )

        ]
