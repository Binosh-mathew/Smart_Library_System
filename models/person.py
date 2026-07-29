class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Email: {self.email}")   
