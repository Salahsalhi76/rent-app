from fastapi import FastAPI
from . import schemas, models
from .database import engine
from .routers import annonce, user, favannonce, authentification

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(annonce.router)
app.include_router(user.router)
app.include_router(favannonce.router)
app.include_router(authentification.router)


   

    
