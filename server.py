
from flask import Flask, render_template, url_for, request
import dbConexion

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def principal():  
    resultados = ""
    return render_template('index.html', mes=resultados)

def error(err):
    return render_template('error_404.html')

@app.route('/consultar')
def consulta():
    resultados = dbConexion.queryTable()
    return render_template('index.html', mes=resultados)

@app.route('/formulario')
def registro():
    return render_template('formulario.html')

@app.route('/ingresar', methods=['get', 'post'])
def ingresar():
    nombre = request.form.get('name')
    apellido = request.form.get('lastname')
    cedula = request.form.get('idcard')
    dbConexion.introduceRecord(nombre, apellido, cedula)
    return render_template('confirmacion.html')

if __name__ == '__main__':
    app.register_error_handler(404, error)
    app.run(debug=True, port=3000)