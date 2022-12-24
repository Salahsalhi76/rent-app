from fastapi import FastAPI, Depends, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/Annonce', status_code=status.HTTP_201_CREATED)
def add_annonce(request: schemas.Annonce, db: Session = Depends(get_db)):
    new_annonce = models.Annonce(
        email = request.email,
        categ = request.categ,
        type = request.type,
        surface = request.surface,
        descr = request.descr,
        prix = request.prix,
        contact = request.contact,
        localisation = request.localisation
    )
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return new_annonce

@app.get('/Annonce')
def get_annonce(db: Session = Depends(get_db)):
    annonces = db.query(models.Annonce).all()
    return annonces

@app.delete('/Annonce/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_Fav(id, db: Session = Depends(get_db)):
    db.query(models.Annonce).filter(models.Annonce.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'

@app.post('/Favoris', status_code=status.HTTP_201_CREATED)
def add_favoris(request: schemas.Annonce, db: Session = Depends(get_db)):
    new_annonce = models.AnnonceFavoris(
        email = request.email,
        categ = request.categ,
        type = request.type,
        surface = request.surface,
        descr = request.descr,
        prix = request.prix,
        contact = request.contact,
        localisation = request.localisation
    )
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return new_annonce

@app.get('/Favorie')
def get_favoris(db: Session = Depends(get_db)):
    AnnoncesFav = db.query(models.AnnonceFavoris).all()
    return AnnoncesFav

@app.delete('/Favorie/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_Fav(id, db: Session = Depends(get_db)):
    db.query(models.AnnonceFavoris).filter(models.AnnonceFavoris.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'
