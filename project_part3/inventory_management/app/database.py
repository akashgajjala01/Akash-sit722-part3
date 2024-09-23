from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://db_4148_sit722_part3_tjft_user:twu5LKN3RvZ30QrDe8K0eIxxOlfn7eBi@dpg-crmbque8ii6s73an990g-a.oregon-postgres.render.com/db_4148_sit722_part3_tjft"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
