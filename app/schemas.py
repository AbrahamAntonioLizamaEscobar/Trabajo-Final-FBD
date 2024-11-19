from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True

class ProyectoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class ProyectoCreate(ProyectoBase):
    pass

class Proyecto(ProyectoBase):
    id: int

    class Config:
        from_attributes = True

class BitacoraBase(BaseModel):
    id_usuario: int
    id_proyecto: int
    actividad: str

class BitacoraCreate(BitacoraBase):
    pass

class Bitacora(BitacoraBase):
    id: int
    fecha: Optional[str] = None

    class Config:
        from_attributes = True

class LogBase(BaseModel):
    id_usuario: int
    accion: str

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: int
    fecha: Optional[str] = None

    class Config:
        from_attributes = True

class GasolineraBase(BaseModel):
    nombre: str
    direccion: str

class GasolineraCreate(GasolineraBase):
    pass

class Gasolinera(GasolineraBase):
    id: int

    class Config:
        from_attributes = True

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    id: int

    class Config:
        from_attributes = True

class VehiculoBase(BaseModel):
    modelo: str
    marca: str
    year: int

class VehiculoCreate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id: int

    class Config:
        from_attributes = True
