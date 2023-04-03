import os
from flask_restx import Resource, Namespace, Api
from flask import Flask, request, jsonify
from utils import filters

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

data_ns = Namespace('perform_query')
api = Api(app)
api.add_namespace(data_ns)


@data_ns.route("/")
class PerformQuery(Resource):
    def post(self):
        response = request.json
        filename = response["file_name"]
        cmd1 = response["cmd1"]
        value1 = response["value1"]
        cmd2 = response["cmd2"]
        value2 = response["value2"]
        print(os.path.join(DATA_DIR, filename))
        print()
        with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as file:
            data = file.readlines()

        res = filters(file=data, cmd=cmd1, value=value1)
        print(res)
        print()
        res = filters(file=res, cmd=cmd2, value=value2)
        print(res)
        return jsonify(res)


if __name__ == "__main__":
    app.run()
