from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

# Rutas para Bitacora
@router.post("/bitacora/", response_model=schemas.Bitacora)
def create_bitacora(bitacora: schemas.BitacoraCreate, db: Session = Depends(database.get_db)):
    return crud.create_bitacora(db=db, bitacora=bitacora)

@router.get("/bitacora/", response_model=list[schemas.Bitacora])
def read_bitacora(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_bitacora(db=db, skip=skip, limit=limit)

@router.put("/bitacora/{bitacora_id}", response_model=schemas.Bitacora)
def update_bitacora(bitacora_id: int, bitacora: schemas.BitacoraCreate, db: Session = Depends(database.get_db)):
    return crud.update_bitacora(db=db, bitacora_id=bitacora_id, bitacora=bitacora)

@router.delete("/bitacora/{bitacora_id}", response_model=schemas.Bitacora)
def delete_bitacora(bitacora_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_bitacora(db=db, bitacora_id=bitacora_id)

# Rutas para Log
@router.post("/log/", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(database.get_db)):
    return crud.create_log(db=db, log=log)

@router.get("/log/", response_model=list[schemas.Log])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_logs(db=db, skip=skip, limit=limit)

@router.put("/log/{log_id}", response_model=schemas.Log)
def update_log(log_id: int, log: schemas.LogCreate, db: Session = Depends(database.get_db)):
    return crud.update_log(db=db, log_id=log_id, log=log)

@router.delete("/log/{log_id}", response_model=schemas.Log)
def delete_log(log_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_log(db=db, log_id=log_id)

# Rutas para Gasolineras
@router.post("/gasolineras/", response_model=schemas.Gasolinera)
def create_gasolinera(gasolinera: schemas.GasolineraCreate, db: Session = Depends(database.get_db)):
    return crud.create_gasolinera(db=db, gasolinera=gasolinera)

@router.get("/gasolineras/", response_model=list[schemas.Gasolinera])
def read_gasolineras(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_gasolineras(db=db, skip=skip, limit=limit)

@router.put("/gasolineras/{gasolinera_id}", response_model=schemas.Gasolinera)
def update_gasolinera(gasolinera_id: int, gasolinera: schemas.GasolineraCreate, db: Session = Depends(database.get_db)):
    return crud.update_gasolinera(db=db, gasolinera_id=gasolinera_id, gasolinera=gasolinera)

@router.delete("/gasolineras/{gasolinera_id}", response_model=schemas.Gasolinera)
def delete_gasolinera(gasolinera_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_gasolinera(db=db, gasolinera_id=gasolinera_id)

# Rutas para Rol
@router.post("/rol/", response_model=schemas.Rol)
def create_rol(rol: schemas.RolCreate, db: Session = Depends(database.get_db)):
    return crud.create_rol(db=db, rol=rol)

@router.get("/rol/", response_model=list[schemas.Rol])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_roles(db=db, skip=skip, limit=limit)

@router.put("/rol/{rol_id}", response_model=schemas.Rol)
def update_rol(rol_id: int, rol: schemas.RolCreate, db: Session = Depends(database.get_db)):
    return crud.update_rol(db=db, rol_id=rol_id, rol=rol)

@router.delete("/rol/{rol_id}", response_model=schemas.Rol)
def delete_rol(rol_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_rol(db=db, rol_id=rol_id)

