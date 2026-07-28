class Book:

    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def show_info(self):
        print("\nBook Information")
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price  : £{self.price}")
        print(f"Copies : {self.copies}")

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book borrowed successfully.")
        else:
            print("Sorry! No copies available.")

    def return_book(self):
        self.copies += 1
        print("Book returned successfully.")