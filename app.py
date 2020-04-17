from zeep import Client
import requests
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

TOKEN = 'cb48489b-567a-4458-8525-517390fb1220'

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('distance')
parser.add_argument('monnaie')

PRIXKILOMETRE = 0.25

@app.route('/')
def index():
    return render_template('index.html')

class CalculerPrix(Resource):
    def get(self):
        #TODO devise
        args = parser.parse_args()
        prix = float(args['distance']) * PRIXKILOMETRE
        return {'prix': prix}

api.add_resource(CalculerPrix, '/calculerPrix')
