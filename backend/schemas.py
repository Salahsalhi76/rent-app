from typing import Optional
from pydantic import BaseModel

class AnnonceBase(BaseModel):
    categ: str
    type: str
    surface: int
    descr: str
    prix: int
    contact: str
    localisation: str
    
class Annonce(AnnonceBase):
    class Config():
        orm_mode = True    

class showuser(BaseModel):
    name:str
    email:str
    annonces: list[Annonce] = []
    class Config():
        orm_mode = True

class showuserwithoutann(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class showAnnonce(BaseModel):
    categ: str
    type: str
    surface: int
    descr: str
    prix: int
    contact: str
    localisation: str
    owner: showuserwithoutann
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
