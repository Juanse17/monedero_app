from fastapi import FastAPI, HTTPException
import db
import models
import repositorio

app = FastAPI()



@app.get("/usuarios/resumen/")
async def obtener_lista_contactos():
    return repositorio.lista_Usuarios_resumen()



@app.post("/crear/usuario/")
async def crear_usuario(Usuario: db.Usuario):
    operacion_exitosa = db.crear_Usuario(Usuario)
    if operacion_exitosa:
        return {"mensaje": "contacto creado correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="Contacto no pudo ser creado: ya existía un contacto con ")



@app.get("/usuario/")
async def obtener_usuario(id: str):
    Usuario = repositorio.obtener_usuario_con_segmentaciones(id)
    if Usuario is None:
        raise HTTPException(status_code=400, detail='Usuario no encontrado')
    else:
        return Usuario