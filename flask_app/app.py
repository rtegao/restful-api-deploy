from flask import Flask
from flask_restful import Api
from resources.model_gatway import ModelGatway



app = Flask(__name__)
api = Api(app)
api.add_resource(ModelGatway,'/model')


    
    
