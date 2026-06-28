import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#Engine and session setup
engine = create_engine(
    os.environ['DATABASE_URL'],
    echo=True
    )

SessionLocal = sessionmaker(bind=engine)

#Base model for all the models
class Base(DeclarativeBase):
    pass