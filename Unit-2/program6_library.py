class Library:
    def __init__(self, book_name, author, availability):
        self.book_name = book_name
        self.author = author
        self.availability = availability

    def check_out(self):
        if self.availability:
            self.availability = False
            print("Book checked out")
        else:
            print("Book not available")

    def return_book(self):
        self.availability = True
        print("Book returned")

    def display(self):
        if self.availability:
            print(self.book_name, "by", self.author, "is available")
        else:
            print(self.book_name, "by", self.author, "is not available")


book1 = Library("Python Basics", "John Smith", True)

book1.display()
book1.check_out()
book1.display()
book1.return_book()
book1.display()
