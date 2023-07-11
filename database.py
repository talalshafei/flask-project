from sqlalchemy import create_engine, text
import os

connection_str = os.environ['DB_CONNECTION_STR']

engine = create_engine(connection_str, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs