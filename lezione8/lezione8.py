#Daniele Pietropaolo


#Exercise 1: Creating an Abstract Class with Abstract Methods
#Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter method

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():

        pass


    @abstractmethod
    def perimetro():

        pass



class Cerchio(Shape):

    def __init__(self,raggio : float) -> None:
        super().__init__()

        self.raggio : float = raggio


    def area(self):

        area_cerchio  : float =(self.raggio ** 2) * 3,14

        return area_cerchio
    

    def perimetro(self):

        diametro : float = 2 * self.raggio

        perimetro_cerchio : float = diametro * 3,14


        return perimetro_cerchio
    





class Rettangolo(Shape):

    def __init__(self,base : float,altezza : float) -> None:
        super().__init__()

        self.base = base
        self.altezza = altezza


    def area(self):

        area_rettangolo : float = self.base * self.altezza

        return area_rettangolo


    def perimetro(self):


        perimetro : float = (2 * self.base) + (2 * self.altezza)

        return perimetro


r1 = Rettangolo(10,5)

print("\n",r1.area(),"\n")
print("\n",r1.perimetro(),"\n")




print("\n--------------------------------------------------------------------------\n")

########################################################################################

#Exercise 2: Implementing Static Methods
#Create a class MathOperations with a static method add that takes two numbers and returns their sum, and another static method multiply that takes two numbers and returns their product.



class MathOperations:

    def __init__(self) -> None:
        pass

    @staticmethod
    def somma(n1 : int, n2 : int):
        

        s : int = n2 + n1

        return s
    

    @staticmethod
    def moltiplica(n1 : int, n2 : int):

        m : int = n2 * n1

        return m


print("\n",MathOperations.moltiplica(2,3),"\n")
print("\n",MathOperations.somma(3,2),"\n")




print("\n--------------------------------------------------------------------------\n")

########################################################################################
    



# Exercise 3: Library Management System 

# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#     __str__ method to return a string representation of the book.

#     @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending.




class Book:

    def __init__(self,title : str, author : str, isbn : int) -> None:

        self.titolo  = title
        self.autore = author
        self.isbn = isbn




    #prendo le informazioni dell' libro da una stringa
    @classmethod
    def from_string(cls,book_str : str):

        title,author,isbn = book_str.split(",")

        return cls(title,author,isbn)


    def __str__(self) -> str:

        return f"TITOLO: {self.titolo}, AUTORE: {self.autore}, ISBN: {self.isbn} " 


class Member:

    def __init__(self,name : str, member_id) -> None:
        
        self.name = name
        self.member_id = member_id
        self.borrowed_books : list[Book] = []


    @classmethod
    def from_string(cls, member_str : str):

        name,meber_id = member_str.split(",")

        return cls(name,meber_id)
    

    def __str__(self) -> str:
        
        return f"NOME: {self.name}, ID: {self.member_id}"
    


    def borrow_book(self,book : Book):

        self.borrowed_books.append(book)


    def remove_book(self,book : Book):

        self.borrowed_books.remove(book)


class Library:

    def __init__(self,books : list[Book],members : list[Member]) -> None:
        self.books = books
        self.members = members
        self.total_books : int = 0


    def add_book(self,book : Book):

        self.books.append(book)
        self.total_books += 1

    
    def remove_book(self,book : Book):

        self.books.remove(book)
        self.total_books -= 1


    def lend_book(self,book : Book,member : Member):

        if member in self.members \
        and book in self.books \
        and book not in self.members[member.borrowed_books]:
            
            member.borrowed_books.append(book)

















#
book_1 : Book = Book.from_string("Harry Potter,Jk ro,123456789")
print(book_1.__str__(),"\n")

book_2 : Book = Book.from_string("topolino,disney,34521")
print(book_2.__str__(),"\n")
print("---")



member_1 : Member = Member.from_string("giggi,12345")
print(member_1.__str__(),"\n")

member_1.borrow_book(book_1)

print("---")
#















