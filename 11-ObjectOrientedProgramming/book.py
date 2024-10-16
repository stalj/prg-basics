# class definition
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def change_page(self,page):
        self.current_page = page

    def display_info(self):
        print(f"My favourite book is {self.title}.")
        print(f"Written by {self.author}.")
        print(f"This book has {self.pages} pages.")
        if self.is_open:
            print(f"I am just reading the book, page {self.current_page}.")
        else:
            print("I am going to read the book later.")


def main():
    # object creation based on the Book class
    favourite_book = Book(
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling", 223)

    # object manipulation
    favourite_book.open()
    favourite_book.change_page(15)
    favourite_book.display_info()
    favourite_book.close()

if __name__ =="__main__":
    main()
