from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Vehiculo)
def create_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(database.get_db)):
    return crud.create_vehiculo(db=db, vehiculo=vehiculo)

@router.get("/", response_model=list[schemas.Vehiculo])
def read_vehiculos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_vehiculos(db=db, skip=skip, limit=limit)

@router.put("/{vehiculo_id}", response_model=schemas.Vehiculo)
def update_vehiculo(vehiculo_id: int, vehiculo: schemas.VehiculoCreate, db: Session = Depends(database.get_db)):
    return crud.update_vehiculo(db=db, vehiculo_id=vehiculo_id, vehiculo=vehiculo)

@router.delete("/{vehiculo_id}", response_model=schemas.Vehiculo)
def delete_vehiculo(vehiculo_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_vehiculo(db=db, vehiculo_id=vehiculo_id)
