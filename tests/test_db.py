from app.models import JobPosting
from app.database.repository import JobRepository

job = JobPosting(
    title='Data Scientist',
    company='Test Company',
    location='Oslo',
    url='https://example.com',
    description='Python SQL Machine Learning'
)

rep = JobRepository()
rep.insert(job)

print('Job inserted')

for row in rep.get_all():
    print(row)
