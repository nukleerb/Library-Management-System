class Library :

    def __init__(self, listofbooks):

          self.avaiblebooks = listofbooks

seek('Book_list.txt')


print ('Book_list.txt')

open('Book_list.txt')

print (f,(all(Book_list.txt)))


close('Book_list.txt')
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
        self.book = None


    def requestBook(self):
        print("Enter the name of the book you'd like to borrow")
        self.book = input()
        return self.book


    def returnBook(self):

        print("Enter the name of the book you'd like to return")


    self.book = input()




    "return" (self.book)




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




