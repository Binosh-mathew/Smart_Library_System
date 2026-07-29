from models.person import Person

class Member(Person):

    def __init__(self, name, email):
        super().__init__(name, email)
        self._borrowed_books = []

    def show_info(self):
        print("\nMember Information")
        print(f"Name : {self.name}")
        print(f"Email: {self.email}")

        print("Borrowed Books:")

        if not self._borrowed_books:
            print("None")
        else:
            for book in self._borrowed_books:
                print(book.title)

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)            