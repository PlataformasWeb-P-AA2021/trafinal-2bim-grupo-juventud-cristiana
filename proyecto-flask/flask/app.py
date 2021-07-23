from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p> API Edificios </p>"


@app.route("/casas")
def listado_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casas/",
            auth=('ispa16', 'ispa123456'))
    casas = json.loads(r.content)['results']
    datos2 = []
    for d in casas:
        datos2.append({'propietario': obtener_edificio(d['propietario']), 'cuartos':d['cuartos'], 'valor':d['valor'],
        'cuartos':d['cuartos'],'direccion':d['direccion'],'color':d['color'],'pisos':d['pisos'],'barrio': obtener_edificio(d['barrio'])})
    print(casas)
    return render_template("listado_casas.html", casas=datos2)

@app.route("/departamentos")
def listado_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('ispa16', 'ispa123456'))
    casas = json.loads(r.content)['results']
    datos2 = []
    for d in casas:
        datos2.append({'propietario': obtener_edificio(d['propietario']), 'cuartos':d['cuartos'], 'valor':d['valor'],
        'cuartos':d['cuartos'],'direccion':d['direccion'],'mensual':d['mensual'],'barrio': obtener_edificio(d['barrio'])})
    print(casas)
    return render_template("listado_departamentos.html", casas=datos2)
@app.route("/personas")
def listado_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/persona/",
            auth=('ispa16', 'ispa123456'))
    personas = json.loads(r.content)['results']
    return render_template("listado_personas.html", personas=personas,
    )
@app.route("/barrios")
def listado_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
            auth=('ispa16', 'ispa123456'))
    barrios = json.loads(r.content)['results']
    return render_template("listado_barrio.html", barrios=barrios)


# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('ispa16', 'ispa123456'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
