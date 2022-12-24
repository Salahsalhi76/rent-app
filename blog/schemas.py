from pydantic import BaseModel

class Annonce(BaseModel):
    categ: str
    type: str
    surface: int
    descr: str
    prix: int
    contact: str
    localisation: str
    email: str