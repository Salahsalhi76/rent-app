from fastapi import FastAPI
from . import schemas, models
from .database import engine
from .routers import annonce, user, favannonce, authentification
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # React application's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(annonce.router)
app.include_router(user.router)
app.include_router(favannonce.router)
app.include_router(authentification.router)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
