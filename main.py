from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, get_db
import schemas, crud
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project API")

# Endpoint to CREATE Project
@app.post("/projects/", tags=["Project"])
def create_project(
    project: schemas.ProjectCreate, 
    db: Session = Depends(get_db)
):
    added_project = crud.add_project(db, project)
    return  added_project

# Get All Projects
@app.get("/projects/", response_model=List[schemas.Project], tags=["Project"])
def get_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)



@app.get("/")
def read_root():
    return {"Hello": "Welcome to the Project API"}
