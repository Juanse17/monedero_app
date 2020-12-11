from pydantic import BaseModel
import db
from typing import List


class UsuarioResumen(BaseModel):
    id: str
    nombre: str


class UsuarioIn(BaseModel):
    id: str
    nombre: str

class UsuarioConSegmentacion(db.Usuario):
    Segmentaciones: List[db.Segmentacion]