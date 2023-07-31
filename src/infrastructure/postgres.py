from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from typing import Optional, Iterator


conn_str = "postgresql://user:password@postgres-service:5432/jobs"
sql_engine = create_engine(conn_str)
session = sessionmaker(bind=sql_engine,autoflush=False)

def get_session() -> Iterator[Session]:
    """Get a session from database"""
    db_session: Session = session()
    try:
        yield db_session
    finally:
        db_session.close()
        
