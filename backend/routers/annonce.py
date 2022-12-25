from fastapi import APIRouter, Depends, status, HTTPException
from backend.database import get_db
from backend.oauth2 import get_current_user
from .. import schemas, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import annonce


router = APIRouter(
    prefix= '/Annonce',
    tags = ['Annonces']
)

@router.get('/',response_model=List[schemas.showAnnonce])
def get_annonce(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return annonce.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_annonce(ann: schemas.Annonce, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return annonce.create(ann, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return annonce.delete(id, db)

@router.get('/{userID}',response_model=List[schemas.Annonce])
def get_selfannonces(userID:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return annonce.get_by_userid(userID, db)