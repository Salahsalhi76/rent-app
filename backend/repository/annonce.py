from sqlalchemy.orm import Session
from backend import models, schemas
from fastapi import Depends, HTTPException, status
from backend.database import get_db

def get_all(db: Session = Depends(get_db)):
    annonces = db.query(models.Annonce).all()
    return annonces

def create(ann: schemas.Annonce, db: Session = Depends(get_db)):
    new_annonce = models.Annonce(
        categ = ann.categ,
        type = ann.type,
        surface = ann.surface,
        descr = ann.descr,
        prix = ann.prix,
        contact = ann.contact,
        localisation = ann.localisation,
        user_id = 1
    )
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return new_annonce  

def delete(id: int, db: Session = Depends(get_db)):
    ann = db.query(models.Annonce).filter(models.Annonce.id == id)  
    if not ann.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"annonce with id = {id} not found")
    ann.delete(synchronize_session=False)
    db.commit()
    return 'deleted succefully'

def get_by_userid(userID:int, db: Session = Depends(get_db)):
    annonces = db.query(models.Annonce).filter(models.Annonce.user_id == userID).all()
    if annonces == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ther is no annonces with userID = {userID}")
    return annonces