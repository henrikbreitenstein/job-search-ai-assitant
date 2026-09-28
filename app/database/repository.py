from requests import get
from app.database.session import get_connection
from app.models import JobPosting

class JobRepository:

    def insert(self, job):
        
        conn = get_connection()

        conn.execute('''
            INSERT OR IGNORE INTO jobs (
                title,
                company,
                location,
                url,
                description
            )
            VALUES (?, ?, ?, ?, ?)
        ''',
        (
            job.title,
            job.company,
            job.location,
            job.url,
            job.description
        ))

        conn.commit()
        conn.close()

    def get_all(self):
        
        conn = get_connection()

        cursor = conn.execute('''
            SELECT
                id,
                title,
                company,
                location,
                url,
                description
            FROM jobs
        ''')

        rows = cursor.fetchall()

        conn.close()

        jobs = []

        for row in rows:

            jobs.append(
               self._row_to_job(row)
            )

        return jobs

    def exists(self, url):
        
        conn = get_connection()

        cursor = conn.execute('''
            SELECT 1
            FROM jobs
            WHERE url = ?
            LIMIT 1
        ''', (url,))

        result = cursor.fetchone()

        conn.close()

        return result is not None


    def get_unprocessed(self):

        conn = get_connection()

        cursor = conn.execute('''
            SELECT
                id,
                title,
                company,
                location,
                url,
                description
            FROM jobs
            WHERE processed = 0
        ''')

        rows = cursor.fetchall()

        conn.close()

        jobs = []

        for row in rows:

            jobs.append(
               self._row_to_job(row)
            )

        return jobs

    def _row_to_job(self, row):

        return JobPosting(
            id=row[0],
            title=row[1],
            company=row[2],
            location=row[3],
            url=row[4],
            description=row[5]
        )


    def mark_processed(self, job_id):

        conn = get_connection()

        conn.execute('''
            UPDATE jobs
            SET processed = 1
            WHERE id = ?
        ''', (job_id,))

        conn.commit()
        conn.close()

    def add_skill(self, job_id, skill):

        conn = get_connection()

        conn.execute('''
            INSERT OR IGNORE INTO job_skills (
                job_id,
                skill
            )
            VALUES (?, ?)
        ''')

        conn.commit()
        conn.close()

    def get_skills(self, job_id):

        conn = get_connection()

        cursor = conn.execute('''
            SELECT skill
            FROM job_skills
            WHERE job_id = ?
        ''', (job_id,))

        rows = cursor.fetchall()

        conn.close()

        return [row[0] for row in rows]




