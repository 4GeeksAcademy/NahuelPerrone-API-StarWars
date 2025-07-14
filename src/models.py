from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_active: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "fecha_active": self.fecha_active,
            # do not serialize the password, its a security breach
        } 

class Planetas(db.Model):
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
    
class Personajes(db.Model):
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
