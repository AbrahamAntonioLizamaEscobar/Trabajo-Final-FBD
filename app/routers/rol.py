from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Rol)
def create_rol(rol: schemas.RolCreate, db: Session = Depends(database.get_db)):
    return crud.create_rol(db=db, rol=rol)

@router.get("/", response_model=list[schemas.Rol])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_roles(db=db, skip=skip, limit=limit)

@router.put("/{rol_id}", response_model=schemas.Rol)
def update_rol(rol_id: int, rol: schemas.RolCreate, db: Session = Depends(database.get_db)):
    return crud.update_rol(db=db, rol_id=rol_id, rol=rol)

@router.delete("/{rol_id}", response_model=schemas.Rol)
def delete_rol(rol_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_rol(db=db, rol_id=rol_id)
