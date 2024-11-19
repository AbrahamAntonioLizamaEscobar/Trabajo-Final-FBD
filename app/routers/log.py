from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(database.get_db)):
    return crud.create_log(db=db, log=log)

@router.get("/", response_model=list[schemas.Log])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_logs(db=db, skip=skip, limit=limit)

@router.put("/{log_id}", response_model=schemas.Log)
def update_log(log_id: int, log: schemas.LogCreate, db: Session = Depends(database.get_db)):
    return crud.update_log(db=db, log_id=log_id, log=log)

@router.delete("/{log_id}", response_model=schemas.Log)
def delete_log(log_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_log(db=db, log_id=log_id)
