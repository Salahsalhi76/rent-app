from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import models
from blog.database import get_db


def add_fav(id, db: Session = Depends(get_db)):
    ann = db.query(models.Annonce).filter(models.Annonce.id == id).first()
    new_annonce = models.AnnonceFavoris(
        categ = ann.categ,
        type = ann.type,
        surface = ann.surface,
        descr = ann.descr,
        prix = ann.prix,
        contact = ann.contact,
        localisation = ann.localisation
    )
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return new_annonce

def get_fav(db: Session = Depends(get_db)):
    AnnoncesFav = db.query(models.AnnonceFavoris).all()
    return AnnoncesFav

def delete_fav(id, db: Session = Depends(get_db)):
    ann = db.query(models.AnnonceFavoris).filter(models.AnnonceFavoris.id == id)
    if not ann.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"annonce with id = {id} not found")
    ann.delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'