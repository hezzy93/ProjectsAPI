from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(500), index=True, nullable=False)
    image_url = Column(String(255), index=True, nullable=False)
    date_of_creation = Column(DateTime, server_default=func.now(), nullable=False)
