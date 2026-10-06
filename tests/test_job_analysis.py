from app.collectors.fake_nav import FakeNavCollector
from app.llm.analyzer import JobAnalyzer


PROFILE = """
MSc Computational Science

Skills:
- Python
- SQL
- Machine Learning
- PyTorch
- TensorFlow
- Pandas
"""

job = FakeNavCollector().collect()[0]

analyzer = JobAnalyzer()

result = analyzer.analyze(
    PROFILE,
    job
)

print(result)

