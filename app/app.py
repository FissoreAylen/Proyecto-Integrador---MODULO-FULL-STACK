from flask import  Flask, render_template, jsonify

#from flask_mysqldb import mysql



app=Flask(__name__)


app.config['MYSQL_HOSTER'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ispcviajes'

#conexion = MySQL(app)

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/america')
def america():
  return render_template('america.html')
  


@app.route('/europa')
def europa():
  return render_template('europa.html')

@app.route('/argentina')
def argentina():
  return render_template('argentina.html')
@app.route('/asia')
def asia():
  return render_template('asia.html')

@app.route('/africa')
def africa():
  return render_template('africa.html')

@app.route('/islas')
def islas():
  return render_template('/islas.html')

@app.route('/oceania')
def oceania():
  return render_template('oceania.html')

@app.route('/nosotros')
def nosotros():
  return render_template('nosotros.html')  

#@app.route('listarusuario')
#def listar_usuarios():
 #   data={}
  #  try:
   #   cursor=conexion.connection.cursor()
    #  sql="SELECT * from usuario"
     # cursor.execute(sql)
     # usuario=cursor.fetchall()
     # data['mensaje'] = 'exito'
    #except Exception as ex:
     # data['mensaje'] = 'Error ...'
      #return jsonify(data)

if __name__=='__main__' :
   app.run(debug=True, port=5000)

