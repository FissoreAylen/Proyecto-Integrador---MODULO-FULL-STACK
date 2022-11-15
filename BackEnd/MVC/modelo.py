from app import db

class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    mail=db.Column(db.String(50))
    contrasenia=db.Column(db.String(50))

class Preferencias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    pais=db.Column(db.String(50))
    lugar=db.Column(db.String(100))
    mail=db.Column(db.String(50))


