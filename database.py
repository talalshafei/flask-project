from sqlalchemy import create_engine, text
import os

connection_str = os.environ['DB_CONNECTION_STR']

engine = create_engine(connection_str,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs


def load_job(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),
                              {'val': id})
        rows = result.all()
        if len(rows) < 1: return None
        return dict(rows[0]._mapping)


def add_application(job_id, application):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:ji, :fn, :e, :l, :ed, :ex, :r)"
        )

        conn.execute(
            query, {
                "ji": job_id,
                "fn": application['full_name'],
                "e": application['email'],
                "l": application['linkedin_url'],
                "ed": application['education'],
                "ex": application['work_experience'],
                "r": application['resume_url']
            })
