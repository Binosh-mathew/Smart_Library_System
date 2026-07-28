from models.book import Book
from models.member import Member
from models.library import Library


library = Library()

book1 = Book("Python Programming", "Dennis Ritchie", 30, 5)
book2 = Book("Clean Code", "Robert Martin", 40, 3)

member1 = Member("Alice", "alice@gmail.com")
member2 = Member("Bob", "bob@gmail.com")


library.add_book(book1)
library.add_book(book2)

library.register_member(member1)
library.register_member(member2)


library.display_books()

library.display_members()