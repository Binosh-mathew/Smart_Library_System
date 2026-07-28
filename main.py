from models.book import Book

book1 = Book("Python Programming", "Dennis Ritchie", 30, 5)

book1.show_info()

book1.borrow()
book1.show_info()

book1.return_book()
book1.show_info()

