from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.create_usuario(db=db, usuario=usuario)

@router.get("/", response_model=list[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_usuarios(db=db, skip=skip, limit=limit)

@router.put("/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)

@router.delete("/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_usuario(db=db, usuario_id=usuario_id)
