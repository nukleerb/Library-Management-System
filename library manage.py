from dbm.ndbm import library


class Library:

    def __init__(self, listofbooks):
        self.avaiblebooks = listofbooks

    def listofallavaiblebooks(self):
        pass

    def addabook(self, param):
        pass

    def removeabook(self, param):
        pass


print('Book_list.txt')

open('Book_list.txt')


class Book_list:
    txt = None


print((all(Book_list.txt)))


def close(Book_list):
    pass


close('Book_list.txt')

print(""" ======LIBRARY MENU=======

                1. List of all available books
                2. Add a book
                3. Remove a book
                """)
choice = int(input("Enter Choice:"))


class Student:
    @classmethod
    def addBook(cls):
        pass

    @classmethod
    def removeBook(cls):
        pass


if choice == 1:
    library.listofallavaiblebooks()
elif choice == 2:
    library.addabook(Student.addBook())
elif choice == 3:
    library.removeabook(Student.removeBook())


def displayAvailablebooks(self):
    print("The books we have in our library are as follows:")

    print("================================")
    for book in self.avaiblelebooks:
        print(book)


def lendbook(self, requestedBook):
    if requestedBook in self.avaiblebooks:
        print("The book you requested has now been borrowed")
        self.avaiblebooks.remove(requestedBook)
    else:
        print("Sorry the book you have requested is currently not in the library")


def addbook(self, returnedBook):
    self.avaiblebooks.append(returnedBook)
    print("Thanks for returning your borrowed book")


class Student:
    book: (str)

    def __init__(self):
        # noinspection PyTypeChecker
        self.book = None

    def requestBook(self):
        print("Enter the name of the book you'd like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you'd like to return")

    returnBook.book = input()

    "return"


def main():
    library = Library(["Nutuk,Mustafa Kemal Atatürk,,", "Faust,Goethe", "Kiralık Konak,Yakup Kadri Karaosmanoğlu"])
    student = Student()
    done = False
    while not done:
        print(""" ======LIBRARY MENU=======
                  1. List of all available books
                  2. Add a book
                  3. Remove a book
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.listofallavaiblebooks()
        elif choice == 2:
            library.addabook(student.addBook())
        elif choice == 3:
            library.removeabook(student.removeBook())
