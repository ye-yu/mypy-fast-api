from typing import Any, Generator
from fastapi import HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import ResultProxy
from src.config.config_service import get_config_service

config_service = get_config_service()

engine = create_engine(config_service.env.db_url)


def get_database() -> Generator[Session, Any, Any]:
    session_maker = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)
    db: Session = session_maker()
    try:
        res: ResultProxy = db.execute(text("SELECT 1"))
        row = res.first()
        if row is None:
            db.close()
            raise HTTPException(502)
        assert row[0] == 1
        yield db
    finally:
        db.close()
