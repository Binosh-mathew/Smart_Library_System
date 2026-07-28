from models.book import Book
from models.member import Member


book1 = Book("Python Programming", "Dennis Ritchie", 30, 5)

member1 = Member("Alice", "alice@gmail.com")

member1.borrowed_books.append(book1)

member1.show_info()