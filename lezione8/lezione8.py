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

    def __init__(self )-> None:
        self.books : list[Book]= []
        self.members : list[Member]=[]
        self.total_books : int = 0


    def add_book(self,book : Book):

        self.books.append(book)
        self.total_books += 1

    
    def remove_book(self,book : Book):

        self.books.remove(book)
        self.total_books -= 1


    def register_member(self,member):

        self.members.append(member)


    def lend_book(self,book : Book,member : Member):

        if member in self.members \
        and book in self.books \
        and book not in member.borrowed_books:
            
            member.borrowed_books.append(book)




#
book_1 : Book = Book.from_string("Harry Potter,Jk ro,123456789")
print(book_1,"\n")

book_2 : Book = Book.from_string("topolino,disney,34521")
print(book_2)
print("---")



member_1 : Member = Member.from_string("giggi,12345")
print(member_1,"\n")

member_1.borrow_book(book_1)

print("---")


lib = Library()

lib.add_book(book_1)
lib.add_book(book_2)

lib.register_member(member_1)


lib.lend_book(book_1,member_1)
lib.remove_book(book_2)


print(lib.books,lib.members)
#




print("\n--------------------------------------------------------------------------\n")

########################################################################################
    


# Exercise 4: University Management System


# Create a system to manage a university with departments, courses, professors, and students. 

# Create an abstract class Person:
# Attributes:

#     name (string)
#     age (int)

# Methods:

#     __init__ method to initialize the attributes.
#     Abstract method get_role to be implemented by subclasses.
#     __str__ method to return a string representation of the person.

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.


# Create a class Course:
# Attributes:

#     course_name (string)
#     course_code (string)
#     students (list of Student instances)
#     professor (Professor instance)

# Methods:

#     __init__ method to initialize the attributes.
#     add_student(student) to add a student to the course.
#     set_professor(professor) to set the professor for the course.
#     __str__ method to return a string representation of the course.

# Create a class Department:

# Attributes:

#     department_name (string)
#     courses (list of Course instances)
#     professors (list of Professor instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_course(course) to add a course to the department.
#     add_professor(professor) to add a professor to the department.
#     __str__ method to return a string representation of the department.

# Create a class University:

# Attributes:

#     name (string)
#     departments (list of Department instances)
#     students (list of Student instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_department(department) to add a department to the university.
#     add_student(student) to add a student to the university.
#     __str__ method to return a string representation of the university.


# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.




###
class Course:
    def __init__(self,course_name : str,course_code : str) -> None:
        
        self.course_name = course_name
        self.course_code = course_code
        self.students : list[Student] = []
        self.professors : list[Professor] = []



    def add_student(self,student):

        self.students.append(student)

    def set_professor(self,professor):

        self.professors.append(professor)


    def __str__(self) -> str:
        
        return f"NOME CORSO: {self.course_name} ID: {self.course_code}" \
            f"LISTA STUDENTI: {self.students}, LISTA PROFESSORI DEL CORSO: {self.professors}"


###
class Department:

    def __init__(self,department_name = str) -> None:
        
        self.department_name : str = department_name
        self.courses : list[Course] = []
        self.professors : list[Professor] = []


    def add_course(self,course):

        self.courses.append(course)

    def set_professor(self,professor):

        self.professors.append(professor)


    def __str__(self) -> str:
        
        return f"NOME DIPARTIMENTO: {self.department_name}" \
            f"LISTA CORSI: {self.courses}, LISTA PROFESSORI DEL CORSO: {self.professors}"



###
class Person(ABC):

    def __init__(self,name : str,age : int) -> None:

        self.name = name
        self.age = age

    @abstractmethod
    def get_role():

        pass

    def __str__(self) -> str:


        return f"Nome : {self.name}, Eta : {self.age} "
    
    

    
###
class Student(Person):
    def __init__(self,student_id : str,name : str,age : int) -> None:
        super().__init__(name,age)


        self.student_id = student_id
        self.courses : list[Course] = []
        self.name = name
        self.age = age



    def get_role():
        
        return "Student"



    def enroll(self,course):

        self.courses.append(course)



###
class Professor(Person):
    def __init__(self,name : str,age : int, professor_id : str, department : str)-> None:
        super().__init__(name, age)

        self.professor_id  : str = professor_id
        self.department  : str = department
        self.courses : list[Course] = []
        self.name = name
        self.age = age




    def assign_to_course(self,course):

        self.courses.append(course)


    def get_role():
        
        return "Professor"




###
class University:

    def __init__(self,name : str) -> None:
        
        self.name = name
        self.departments : list[Department] = []
        self.students : list[Student] = []


    
    def add_student(self,student):

        self.students.append(student)


    def add_student(self,student):

        self.students.append(student)


    def add_department(self,department):

        self.departments.append(department)




    """def __str__(self) -> str:
        lista_nomi:list[str]=[]
        for i in self.departments:
            lista_nomi.append(i.department_name)
        return f"nome Universita: {self.name},\ndipartimenti: {lista_nomi},\nStudenti: {self.students}"
"""


    def __str__(self) -> str:
        
        
        l_dip = [i.department_name for i in self.departments]

        l_cor = [j.course_name for i in self.departments for j in i.courses]
        print(l_cor)

        dipartimenti = " ".join(l_dip)
        corsi = " ".join(l_cor)
        return f"Nome universita: {self.name},\nNome dipartimenti: {dipartimenti},\nNome corsi: {corsi}"




        
        








#
corso_1 = Course("ingenieria","12334")
corso_2 = Course("medicina","45678")

studente_1 = Student("sjsjsjs","111111",22)
studente_2 = Student("jsjsjsjs","22222",12)
studente_3 = Student("jdjdfjfd","3333",23)
studente_4 = Student("ajdiofn","4444",21)
studente_5 = Student("dijfier","55555",32)
studente_6 = Student("hikjbhgg","66666",26)

professore_1 = Professor("1111",45,"1234","dipartimento 1")
professore_2 = Professor("2222",46,"9876","dipartimento 2")

diparimento_1 = Department("dipartimento 1")
dipartimento_2 = Department("dipartimento 2")


uni = University("ltsgooo")

uni.add_student(studente_1)
uni.add_student(studente_2)
uni.add_student(studente_3)
uni.add_student(studente_4)
uni.add_student(studente_5)
uni.add_student(studente_6)

uni.add_department(diparimento_1)
uni.add_department(dipartimento_2)


print(uni)


print()