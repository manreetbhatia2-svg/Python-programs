from abc import ABC, abstractmethod
class Library(ABC):
    def __init__(self,book_name,author):
        self.book_name = book_name
        self.author = author

    @abstractmethod
    def charges(self):
        pass

    def interface(self):
        return f"Book: {self.book_name}, Author: {self.author}"
    
class PrintedBook(Library):
    def __init__(self,book_name,author,availability):
        super().__init__(book_name,author)
        self.__availability = availability

    def charges(self):
        return("Borrowing charges for printed book is Rs.20 ")
    
class EBook(Library):
    def charges(self):
        return("Borrowing charges for E-Book is Rs.10 ")
    
mybook = PrintedBook("You Can Win","Shiv Khera",15)
myEbook = EBook("Vistas","Rina Sharma")

print(mybook.charges())
print(mybook.interface())

print(myEbook.charges())
print(myEbook.interface())