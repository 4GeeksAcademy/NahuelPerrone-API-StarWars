from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_active: Mapped[str] = mapped_column(nullable=False)

    # planetas_favoritos_id = mapped_column(ForeignKey("planetas_favoritos.id"))
    # planetas_favoritos = relationship("Planetas_favoritos", back_populates="user")

    # planetas_favoritos = relationship("Planetas_favoritos", back_populates="user")

    # personajes_favoritos_id = mapped_column(ForeignKey("personajes_favoritos.id"))
    # personajes_favoritos = relationship("Personajes_favoritos", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "fecha_active": self.fecha_active,
            # do not serialize the password, its a security breach
        } 

    # def __str__(self): 
    #     return self.nombre

class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    caracteristicas: Mapped[str] = mapped_column(nullable=False)
    region: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    habitantes: Mapped[str] = mapped_column(nullable=False)
    diametro: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "caracteristicas": self.caracteristicas,
            "region": self.region,
            "habitantes": self.habitantes,
            "diametro": self.diametro,
            # do not serialize the password, its a security breach
        } 
    

    
class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    cualidad: Mapped[str] = mapped_column(nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(nullable=False)
    altura: Mapped[str] = mapped_column(nullable=False)
    color_de_cabello: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cualidad": self.cualidad,
            "color_de_ojos": self.color_de_ojos,
            "altura": self.altura,
            "color_de_cabello": self.color_de_cabello,
            # do not serialize the password, its a security breach
        }
    

class Planetas_favoritos(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(nullable=False)
    planeta_id: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

    # user = relationship("User", back_populates="planetas_favoritos")

    # user_id = mapped_column(ForeignKey("user.id"))
    # user = relationship("User", back_populates="planetas_favoritos")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta_id": self.planeta_id
        
        } 
    
    
class Personajes_favoritos(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(nullable=True)
    personaje_id: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

    # user = relationship("User", back_populates="personajes_favoritos")
   
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "name":self.name
        }
    

