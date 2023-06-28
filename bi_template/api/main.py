from flask import request
from flask_restful import Resource
from .instance import server

app, api = server.app, server.api


class Test(Resource):
    def get(self):
        data = request.get_json()
        print(data["username"])


api.add_resource(Test, '/test/')