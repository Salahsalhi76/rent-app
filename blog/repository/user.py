from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from blog import models, schemas
from passlib.context import CryptContext
from blog.database import get_db



pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto",)


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedPassword = pwd_cxt.hash(request.password)  
    new_user = models.User(
        email = request.email,
        name = request.name,
        password = hashedPassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id = {id} not found")
    return user