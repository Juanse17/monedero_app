import models
import db


def obtener_usuario_con_segmentaciones(id: str):
    Usuario = db.obtener_Usuario_por_id(id)
    if Usuario is None:
        return None
    Segmentaciones = db.obtener_segmentaciones_de_usuario(id)
    #contacto_con_telefonos = models.ContactoConTelefono(id=contacto.id, nombre=contacto.nombre, direccion=contacto.direccion, telefonos=telefonos)
    Usuario_con_Segmentaciones = models.UsuarioConSegmentacion(
        **Usuario.dict(), Segmentaciones=Segmentaciones)
    return Usuario_con_Segmentaciones

def lista_Usuarios_resumen():
    lista_Usuarios_resumen = []
    Usuarios = db.obtener_Usuarios()
    for id, Usuario in Usuarios.items():
        Usuario_resumen = models.UsuarioResumen(
            id=Usuario.id, nombre=Usuario.nombre)
        lista_Usuarios_resumen.append(Usuario_resumen)
    return lista_Usuarios_resumen