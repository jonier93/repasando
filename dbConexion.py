from dis import Instruction
import sqlite3

connection = sqlite3.connect('dataBase.db', check_same_thread=False) # check_same_thread es necesaria para evitar error al invocar desde el server
cur = connection.cursor()
#instruction = "CREATE DATABASE dataBase"
#instruction = "CREATE TABLE usuarios (nombre VARCHAR(20) NOT NULL, apellido VARCHAR(20), cedula INT PRIMARY KEY);"

instSQL=""

def introduceRecord(nombre, apellido, cedula):
    global instSQL # Permite modificar una variable global dentro de una función
    instSQL = "INSERT INTO usuarios (nombre, apellido, cedula) VALUES ('" + nombre + "', '" + apellido + "', " + cedula + ");"
    cur.execute(instSQL)
    connection.commit() #Guardar datos

def updateRecord():
    global instSQL
    instSQL = "UPDATE usuarios SET nombre='Floky' WHERE nombre='Flonshy';"
    cur.execute(instSQL)
    connection.commit() #Guardar datos

def queryTable():
    global instSQL
    instSQL = "SELECT * FROM usuarios;"
    cur.execute(instSQL)
    resultados = cur.fetchall()
    print(resultados)
    return resultados


    