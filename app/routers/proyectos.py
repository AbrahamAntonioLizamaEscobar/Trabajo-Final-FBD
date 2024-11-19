from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Proyecto)
def create_proyecto(proyecto: schemas.ProyectoCreate, db: Session = Depends(database.get_db)):
    return crud.create_proyecto(db=db, proyecto=proyecto)

@router.get("/", response_model=list[schemas.Proyecto])
def read_proyectos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_proyectos(db=db, skip=skip, limit=limit)

@router.put("/{proyecto_id}", response_model=schemas.Proyecto)
def update_proyecto(proyecto_id: int, proyecto: schemas.ProyectoCreate, db: Session = Depends(database.get_db)):
    return crud.update_proyecto(db=db, proyecto_id=proyecto_id, proyecto=proyecto)

@router.delete("/{proyecto_id}", response_model=schemas.Proyecto)
def delete_proyecto(proyecto_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_proyecto(db=db, proyecto_id=proyecto_id)
