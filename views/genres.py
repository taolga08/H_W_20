from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

    def post(self):
        req_json = request.json
        ent = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{ent.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return GenreSchema().dump(genre), 200

    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def patch(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.partially_update(req_json)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
