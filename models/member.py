class Member:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def show_info(self):
        print("\nMember Information")
        print(f"Name : {self.name}")
        print(f"Email: {self.email}")

        print("Borrowed Books:")

        if not self.borrowed_books:
            print("None")
        else:
            for book in self.borrowed_books:
                print(book.title)