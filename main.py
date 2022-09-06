from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

constantesVolumen = {
  "m3": 1,
  "bl": 6.2898,
  "ft3": 35.31,
  "gl": 264,
  "lt": 1000
}

constantesTemperatura = {
  "kelvin": 0,
  "celsius": 273.15,
  "fahrenheit": 459.67,
  "rankine": 0
}

@app.route("/calculadora", methods=["POST"])
def calculadora():
  # el tipo de cálculo
  tipo = request.json['tipo']
  # la cantidad a convertir
  cantidad = request.json['cantidad']
  # la unidad de medida de la cantidad
  unidad = request.json['unidad']
  # la unidad de medida a la cual convertir
  convertirUnidad = request.json['convertirUnidad']

  conversor = constantesTemperatura
  resultado = 0
  if tipo == 'volumen':
    conversor = constantesVolumen
    resultado = cantidad * conversor[convertirUnidad] / conversor[unidad]
  else:
    resultado = cantidad + conversor[unidad] - conversor[convertirUnidad]

  response = jsonify(resultado=resultado)
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/public/<path>')
def send_report(path):
    return send_from_directory('public', path)