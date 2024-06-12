from fastapi import FastAPI
from Routes import usuario
from Routes import routes

app = FastAPI()

app.include_router(usuario.router, tags=['usuario'])
app.include_router(routes.router, tags=['routes'])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)