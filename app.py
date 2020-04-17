from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

# Create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('devise')
parser.add_argument('distance')

prixkm = 0.25


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')


class CalculPrix(Resource):
    def get(self):
        # TODO devise
        args = parser.parse_args()
        if args['devise'] == 'Euro':
            prix = float(args['distance']) * prixkm
            return prix
        elif args['devise'] == 'Dollar':
            prix = float(args['distance']) * prixkm * 1.09
            return prix
        elif args['devise'] == 'Yen':
            prix = float(args['distance']) * prixkm * 116.702
            return prix


api.add_resource(CalculPrix, '/CalculPrix')
