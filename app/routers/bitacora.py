from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Bitacora)
def create_bitacora(bitacora: schemas.BitacoraCreate, db: Session = Depends(database.get_db)):
    return crud.create_bitacora(db=db, bitacora=bitacora)

@router.get("/", response_model=list[schemas.Bitacora])
def read_bitacora(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_bitacora(db=db, skip=skip, limit=limit)

@router.put("/{bitacora_id}", response_model=schemas.Bitacora)
def update_bitacora(bitacora_id: int, bitacora: schemas.BitacoraCreate, db: Session = Depends(database.get_db)):
    return crud.update_bitacora(db=db, bitacora_id=bitacora_id, bitacora=bitacora)

@router.delete("/{bitacora_id}", response_model=schemas.Bitacora)
def delete_bitacora(bitacora_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_bitacora(db=db, bitacora_id=bitacora_id)
