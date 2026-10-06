import sqlite3

DATABASE_PATH = 'data/jobs.db'

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def add_column_if_missing(conn, name, definition):

    columns = [
        row[1]
        for row in conn.execute(
            "PRAGMA table_info(jobs)"
        )
    ]

    if name not in columns:
        conn.execute(
            f"ALTER TABLE jobs ADD COLUMN {name} {definition}"
        )

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
            skill_score REAL DEFAULT 0,
            fit_score REAL DEFAULT 0,
            seniority TEXT,
            years_experience INTEGER,
            analysis TEXT,
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


