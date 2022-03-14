from flask_restful import Resource
from models.stores import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.get_by_name(name)

        if store:
            return store.json()
        return {'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A Store with a name "{}" already exist'.format(name)}, 400

        store = StoreModel(name)
        try:
            StoreModel.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(name)

        return {'message': 'Store deleted successfully'}, 200


class StoreList(Resource):
    def get(self):
        return {'store': store.json() for store in StoreModel.query.all()}