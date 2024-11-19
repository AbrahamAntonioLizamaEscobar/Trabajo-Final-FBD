from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Gasolinera)
def create_gasolinera(gasolinera: schemas.GasolineraCreate, db: Session = Depends(database.get_db)):
    return crud.create_gasolinera(db=db, gasolinera=gasolinera)

@router.get("/", response_model=list[schemas.Gasolinera])
def read_gasolineras(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_gasolineras(db=db, skip=skip, limit=limit)

@router.put("/{gasolinera_id}", response_model=schemas.Gasolinera)
def update_gasolinera(gasolinera_id: int, gasolinera: schemas.GasolineraCreate, db: Session = Depends(database.get_db)):
    return crud.update_gasolinera(db=db, gasolinera_id=gasolinera_id, gasolinera=gasolinera)

@router.delete("/{gasolinera_id}", response_model=schemas.Gasolinera)
def delete_gasolinera(gasolinera_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_gasolinera(db=db, gasolinera_id=gasolinera_id)
