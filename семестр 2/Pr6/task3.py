class Book:
    def __init__(self, name, author, count=1):
        self.name, self.author, self.count = name, author, count

    def __str__(self):
        return f"{self.name} ({self.author}) - {self.count} шт."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        for b in self.books:
            if b.name == new_book.name and b.author == new_book.author:
                b.count += new_book.count
                return
        self.books.append(new_book)

    def user_take_book(self, name, author):
        for b in self.books:
            if b.name == name and b.author == author:
                if b.count > 0:
                    b.count -= 1
                else:
                    print("Книг більше немає")
                return
        print("Такої книги немає")

    def show_books(self):
        for b in self.books:
            print(b)

lib = Library()
lib.add_book(Book("Python", "Guido", 2))
lib.add_book(Book("Python", "Guido", 1))

lib.show_books()
lib.user_take_book("Python", "Guido")
lib.user_take_book("C++", "Stroustrup")
lib.show_books()