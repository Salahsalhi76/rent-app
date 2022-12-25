from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Annonce(Base):
    __tablename__ = 'annonces'

    id = Column(Integer, primary_key = True, index= True)
    categ = Column(String)
    type = Column(String)
    surface = Column(Integer)
    descr = Column(String)
    prix = Column(Integer)
    contact = Column(String)
    localisation = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates= "annonces")

class AnnonceFavoris(Base):
    __tablename__ = 'AnnImob_Fav'
    
    id = Column(Integer, primary_key = True, index= True)
    categ = Column(String)
    type = Column(String)
    surface = Column(Integer)
    descr = Column(String)
    prix = Column(Integer)
    contact = Column(String)
    localisation = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    annonces = relationship("Annonce", back_populates= "owner")
    