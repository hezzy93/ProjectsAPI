from sqlalchemy.orm import Session
import schemas, models


# Create Project
def add_project(db:Session, project: schemas.ProjectCreate):
    db_project = models.Project(
        title=project.title,
        description=project.description,
        image_url=project.image_url,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


#Get All Projects
def get_projects(db: Session):
    return db.query(models.Project).all()