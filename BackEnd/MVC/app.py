from flask import Flask
#conexión con la base de datos
from sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='Clave secreta'
app.config['SQLALCHEMY_DATABASE_URI']='mysql:///database/sitio_web.db'

db=SQLAlchemy(app)

from controlador import *

if __name__=='__main__':
    app.run(debug=True)

