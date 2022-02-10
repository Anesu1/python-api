from flask_restful import Resource

class BookList(Resource):
    def get(self):
        return {'hello': 'from booklist'}