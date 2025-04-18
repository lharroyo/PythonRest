from flask import Flask, jsonify, request

#Definir una instancia de Flask
app = Flask(__name__)
#Habilitar el modo de depuración
app.config["DEBUG"] = True

#Creamos un endpoint para la ruta /
@app.route('/', methods=['GET'])
#Definimos la función home que es la que se ejecutará cuando se acceda a la ruta /
def home():
    #Retornamos un mensaje en formato JSON
    return jsonify({"message":"Este es el metodo GET"})

@app.route('/', methods=['POST'])
def post_home():
    return jsonify({"message":"Este es el metodo POST"})

@app.route('/', methods=['PUT'])
def put_home():
    return jsonify({"message":"Este es el metodo PUT"})

@app.route('/', methods=['DELETE'])
def delete_home():
    return jsonify({"message":"Este es el metodo DELETE"})


app.run()