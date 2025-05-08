from sqlalchemy import String, Column, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.dialects.postgresql import UUID
import uuid
import os
from dotenv import load_dotenv

load_dotenv("user_service\.env")

engine = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False, unique = True)
    email = Column(String)
    password = Column(String, nullable = False)

# Base.metadata.create_all(engine)
Session = sessionmaker(engine)

session = Session()