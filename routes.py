from flask_restful import Resource
from repository import Repository

repo = Repository()

class BookList(Resource):
    def get(self):
        return [book.__dict__ for book in repo.books_get_all()]
    
class Book(Resource):
    def get(self, book_id):
        return {'hello': 'from book {book_id}'}
    
class ReviewList(Resource):
    def get(self):
        return {'hello': 'from reviews'}
    
class Review(Resource):
    def get(self, review_id):
        return {'hello': 'from review {review_id}'}