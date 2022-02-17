from flask import Flask
from flask_restful import Api
from routes import BookList, ReviewList, Book, Review

BASE_URL = '/api'

app = Flask(__name__)
api = Api(app)

api.add_resource(BookList, f'{BASE_URL}/BookList')
api.add_resource(Book, f'{BASE_URL}/Books/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/ReviewList')
api.add_resource(Review, f'{BASE_URL}/Review/<review_id>')


@app.route('/')
def hello_world():
    return 'Hello, Flask World!'

# export FLASK_APP=app.py

if __name__ == '__main__':
    app.run(debug=True)