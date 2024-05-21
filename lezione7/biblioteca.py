#daniele Pietropaolo

class Book:
    def __init__(self,book_id,title,autor) -> None:
        self.book_id : str = book_id
        self.title : str = title
        self.autor : str = autor
        self.is_borrowed : bool = False

    def borrow(self):
        if self.is_borrowed == False:

            self.is_borrowed = True

    def return_book(self):

        if self.is_borrowed == True:

            self.is_borrowed = False




class Member:
    def __init__(self, member_id : str,name : str):

        self.member_id : str = member_id
        self.name : str = name
        self.borrowed_books : list[Book] = []


    def borrow_book(self, book : Book):

        if book == True and book in self.borrowed_books:
            pass

        else:
            self.borrowed_books.append(book)
            book.is_borrowed = False


    def return_book(self,book : Book):

        
        if book == False and len(self.borrowed_books) <= 0 and not self.borrowed_books:
            pass

        else: 
            self.borrowed_books.remove(book)
            book.is_borrowed = True



class Library:
    def __init__(self) -> None:

        self.books : dict[str,Book] = {}
        self.members : dict[str,Member] = {}
        

    def add_book(self,book_id: str, title: str, author: str): 
        
        if book_id not in self.books.keys():

           # b : Book = Book(book_id, title, author)
           # self.books[book_id] = b
        
            self.books[book_id] = Book(book_id, title, author)



    def register_member(self,member_id:str, name: str):

        if member_id not in self.members:


         self.members[member_id] = Member(member_id,name)
        
        


    def borrow_book(self,member_id: str, book_id: str):

        if book_id in self.books and member_id in self.members:
    
            member = self.members[member_id]
            book = self.books[book_id]

            member.borrow_book(book)
        
        


    def return_book(self,member_id: str, book_id: str): 

        if book_id in self.books and member_id in self.members:
    
            member = self.members[member_id]
            book = self.books[book_id]

            member.return_book(book)


            

    
    def get_borrowed_books(self,member_id):
        t = []

        if member_id in self.members:


            l = self.members[member_id]


            for book in l.borrowed_books:
                t.append(book.title)
        
        return t
    




library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))






