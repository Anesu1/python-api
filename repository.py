from models import BookModel, ReviewModel

book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)

class Repository():
    def books_get_all(self):
        return [book1, book2]
    def book_get_by_id(self, book_id):
        books=[book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    