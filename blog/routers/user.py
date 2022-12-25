from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import get_db
from ..repository import user

router = APIRouter(
    prefix= '/user',
    tags= ['User']
)


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model= schemas.showuser)
def get_user(id:int , db: Session = Depends(get_db)):
    return user.get_user(id, db)