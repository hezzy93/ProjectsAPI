from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Project schema for creating new projects
class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: str

    model_config = ConfigDict(from_attributes=True)

class ProjectCreate(ProjectBase):
    pass
    model_config = ConfigDict(from_attributes=True)

class Project(ProjectBase):
    id: int
    date_of_creation: datetime
