from app import app
from modelo import *
from flask import render_template

@app.route('/')
def index():
    #listas
    usuario=Usuario.query.all()
    preferencia=Preferencias.query.all()
    usuario_preferencias=[]
    for usuario in usuario:
        total_preferencias=[]
        for preferencias in preferencia:
            if(preferencias.mail==usuario.mail):
                total_preferencias+=preferencia.pais+preferencia.lugar
        usuario_preferencias+=[[usuario.nombre,total_preferencias]]
    return render_template('index.html',list=usuario_preferencias)

