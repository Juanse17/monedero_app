from pydantic import BaseModel
from datetime import datetime
from typing import Dict


class Usuario(BaseModel):
    id: str
    nombre: str
    username: str
    password: str
    email: str
    direccion: str

class Segmentacion(BaseModel):
    id: int
    Clasificacion: str
    Saldo: str
    Usuario_id: str


Usuarios: Dict[str, Usuario]

Usuarios = {
    "1": Usuario(id="1", nombre="Alejandro", username="alejo14", password="root", email="alejandro@gmail.com",direccion="cll3242", ),
    "2": Usuario(id="2", nombre="Angelica", username="yeimi12", password="diego", email="angelica@gmail.com", direccion="cll3242324"),
    "3": Usuario(id="3", nombre="Daniela", username="danilon", password="juanjo08", email="angie@gmail.com", direccion="cll2436"),
    "4": Usuario(id="4", nombre="David", username="domimorte", password="gaia", email="divin@gmail.com", direccion="cll986"),
    "5": Usuario(id="5", nombre="Sebastian", username="juanito", password="kal", email="juanse@gmail.com", direccion="cll6789"),
}

Segmentaciones: Dict[int, Segmentacion]

Segmentaciones = {
    1: Segmentacion(**{"id": 1, "Clasificacion": "Ocio", "Saldo": "500000", "Usuario_id": "1"}),
    2: Segmentacion(**{"id": 2, "Clasificacion": "Arriendo", "Saldo": "2000000", "Usuario_id": "2"}),
    3: Segmentacion(**{"id": 3, "Clasificacion": "Transporte", "Saldo": "240000 ", "Usuario_id": "1"}),
    4: Segmentacion(**{"id": 4, "Clasificacion": "Pareja", "Saldo": "1000000", "Usuario_id": "1"}),
    5: Segmentacion(**{"id": 5, "Clasificacion": "Servicios", "Saldo": "680000", "Usuario_id": "2"}),
    6: Segmentacion(**{"id": 6, "Clasificacion": "Mecato", "Saldo": "200000", "Usuario_id": "3"}),

}


def obtener_segmentaciones_de_usuario(id: str):
    lista_Segmentaciones = []
    for Segmentacion in Segmentaciones.values():
        if Segmentacion.Usuario_id == id:
            lista_Segmentaciones.append(Segmentacion)
    return lista_Segmentaciones



def obtener_Usuarios():
    return Usuarios


def obtener_lista_Usuarios():
    lista_Usuarios = []
    for Usuario in Usuarios:
        lista_Usuarios.append(Usuarios[Usuario])
    return lista_Usuarios


def obtener_Usuario_por_id(id: str):
    if id in Usuarios:
        return Usuarios[id]
    else:
        return None


def crear_Usuario(Usuario: Usuario):
    if Usuario.id in Usuarios:
        return False
    else:
        Usuarios[Usuario.id] = Usuario
        return True
