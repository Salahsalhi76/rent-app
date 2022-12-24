from .database import Base
from sqlalchemy import Column, Integer, String

class Annonce(Base):
    __tablename__ = 'AnnImob'

    email = Column(String)
    id = Column(Integer, primary_key = True, index= True)
    categ = Column(String)
    type = Column(String)
    surface = Column(Integer)
    descr = Column(String)
    prix = Column(Integer)
    contact = Column(String)
    localisation = Column(String)

class AnnonceFavoris(Base):
    __tablename__ = 'AnnImob_Fav'
    
    email = Column(String)
    id = Column(Integer, primary_key = True, index= True)
    categ = Column(String)
    type = Column(String)
    surface = Column(Integer)
    descr = Column(String)
    prix = Column(Integer)
    contact = Column(String)
    localisation = Column(String)
    