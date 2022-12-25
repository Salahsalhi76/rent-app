from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from blog import models
from .. import schemas, database
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    tags=["authentification"]
)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto",)

@router.post('/login')
def login(request: schemas.login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"incorrect password")
    #generate jwt token and return it
    return user