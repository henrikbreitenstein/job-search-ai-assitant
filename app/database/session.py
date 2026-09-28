import sqlite3

DATABASE_PATH = 'data/jobs.db'

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():

    conn = get_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT UNIQUE,
            description TEXT,
            processed INTEGER DEFAULT 0
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS job_skills (
            job_id INTEGER,
            skill TEXT,
            UNIQUE(job_id, skill)
        )
    ''')

    conn.commit()
    conn.close()

