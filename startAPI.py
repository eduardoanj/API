from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from controllers.assinantes_control import AssinanteController

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(AssinanteController, '/api/assinante/', endpoint="assinantes")
api.add_resource(AssinanteController, '/api/assinante/<int:id>', endpoint="assinante")

app.run(debug=True, host="192.168.0.7", port="80")


