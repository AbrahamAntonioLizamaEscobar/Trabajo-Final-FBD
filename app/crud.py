from sqlalchemy.orm import Session
from . import models, schemas

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    fake_hashed_password = usuario.password + "notreallyhashed"
    db_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email, password=fake_hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_usuario.nombre = usuario.nombre
    db_usuario.email = usuario.email
    db_usuario.password = usuario.password
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_usuario)
    db.commit()
    return db_usuario

# CRUD para Proyecto
def get_proyectos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Proyecto).offset(skip).limit(limit).all()

def create_proyecto(db: Session, proyecto: schemas.ProyectoCreate):
    db_proyecto = models.Proyecto(nombre=proyecto.nombre, descripcion=proyecto.descripcion)
    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto

def update_proyecto(db: Session, proyecto_id: int, proyecto: schemas.ProyectoCreate):
    db_proyecto = db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    if db_proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    db_proyecto.nombre = proyecto.nombre
    db_proyecto.descripcion = proyecto.descripcion
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto

def delete_proyecto(db: Session, proyecto_id: int):
    db_proyecto = db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    if db_proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    db.delete(db_proyecto)
    db.commit()
    return db_proyecto

# CRUD para Bitacora
def get_bitacora(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Bitacora).offset(skip).limit(limit).all()

def create_bitacora(db: Session, bitacora: schemas.BitacoraCreate):
    db_bitacora = models.Bitacora(id_usuario=bitacora.id_usuario, id_proyecto=bitacora.id_proyecto, actividad=bitacora.actividad)
    db.add(db_bitacora)
    db.commit()
    db.refresh(db_bitacora)
    return db_bitacora

def update_bitacora(db: Session, bitacora_id: int, bitacora: schemas.BitacoraCreate):
    db_bitacora = db.query(models.Bitacora).filter(models.Bitacora.id == bitacora_id).first()
    if db_bitacora is None:
        raise HTTPException(status_code=404, detail="Bitacora no encontrada")
    db_bitacora.id_usuario = bitacora.id_usuario
    db_bitacora.id_proyecto = bitacora.id_proyecto
    db_bitacora.actividad = bitacora.actividad
    db.commit()
    db.refresh(db_bitacora)
    return db_bitacora

def delete_bitacora(db: Session, bitacora_id: int):
    db_bitacora = db.query(models.Bitacora).filter(models.Bitacora.id == bitacora_id).first()
    if db_bitacora is None:
        raise HTTPException(status_code=404, detail="Bitacora no encontrada")
    db.delete(db_bitacora)
    db.commit()
    return db_bitacora

# CRUD para Log
def get_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Log).offset(skip).limit(limit).all()

def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.Log(id_usuario=log.id_usuario, accion=log.accion)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def update_log(db: Session, log_id: int, log: schemas.LogCreate):
    db_log = db.query(models.Log).filter(models.Log.id == log_id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log no encontrado")
    db_log.id_usuario = log.id_usuario
    db_log.accion = log.accion
    db.commit()
    db.refresh(db_log)
    return db_log

def delete_log(db: Session, log_id: int):
    db_log = db.query(models.Log).filter(models.Log.id == log_id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log no encontrado")
    db.delete(db_log)
    db.commit()
    return db_log
from fastapi import HTTPException

# CRUD para Gasolinera
def get_gasolineras(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Gasolinera).offset(skip).limit(limit).all()

def get_gasolinera_by_id(db: Session, gasolinera_id: int):
    db_gasolinera = db.query(models.Gasolinera).filter(models.Gasolinera.id == gasolinera_id).first()
    if db_gasolinera is None:
        raise HTTPException(status_code=404, detail="Gasolinera no encontrada")
    return db_gasolinera

def create_gasolinera(db: Session, gasolinera: schemas.GasolineraCreate):
    db_gasolinera = models.Gasolinera(nombre=gasolinera.nombre, direccion=gasolinera.direccion, capacidad=gasolinera.capacidad)
    db.add(db_gasolinera)
    db.commit()
    db.refresh(db_gasolinera)
    return db_gasolinera

def update_gasolinera(db: Session, gasolinera_id: int, gasolinera: schemas.GasolineraCreate):
    db_gasolinera = db.query(models.Gasolinera).filter(models.Gasolinera.id == gasolinera_id).first()
    if db_gasolinera is None:
        raise HTTPException(status_code=404, detail="Gasolinera no encontrada")
    db_gasolinera.nombre = gasolinera.nombre
    db_gasolinera.direccion = gasolinera.direccion
    db_gasolinera.capacidad = gasolinera.capacidad
    db.commit()
    db.refresh(db_gasolinera)
    return db_gasolinera

def delete_gasolinera(db: Session, gasolinera_id: int):
    db_gasolinera = db.query(models.Gasolinera).filter(models.Gasolinera.id == gasolinera_id).first()
    if db_gasolinera is None:
        raise HTTPException(status_code=404, detail="Gasolinera no encontrada")
    db.delete(db_gasolinera)
    db.commit()
    return db_gasolinera

