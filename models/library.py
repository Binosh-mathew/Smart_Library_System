class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print(f"{member.name} registered successfully.")

    def display_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\nLibrary Books")

        for book in self.books:
            book.show_info()

    def display_members(self):

        if not self.members:
            print("\nNo members registered.")
            return

        print("\nLibrary Members")

        for member in self.members:
            member.show_info()

    def borrow_book(self, member, book):

        if member not in self.members:
           print("Member is not registered.")
           return

        if book not in self.books:
           print("Book not found in library.")
           return

        if book.copies <= 0:
           print("No copies available.")
           return

        if book in member._borrowed_books:
           print("Member already borrowed this book.")
           return    

        book.borrow()

        member.borrow_book(book)

        print(f"{member.name} borrowed '{book.title}' successfully.")   