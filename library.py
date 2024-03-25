import re
import time
from plyer import notification


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def add_new_users(self):
        print("ID:", self.id, "Name:", self.name)

    def edit(self, new_name):
        self.new_name = new_name
        uname = self.name
        edit = uname.replace(self.name, new_name)
        print("=================================")
        print("The User Name is edited:")
        print("ID:", self.id, "Name:", edit)

    #def delete (self):
        #del_name=self.name





class Book:
    def __init__(self, book_name, author):
        self.avail_book = None
        self.book_name = book_name
        self.author = author

    def add_new_book(self):
        print("Library Books")
        print("==================")
        print("Book Name:", self.book_name, "\nAuthor:", self.author)

    def edit_book(self, new_book, new_author):
        self.new_book = new_book
        self.new_author = new_author
        edit_book = self.book_name
        edit_new_book = edit_book.replace(self.book_name, new_book)
        edit_author = self.author
        edit_new_author = edit_author.replace(self.author, new_author)
        print("EDited Books")
        print("=================")
        print("Book name:", edit_new_book, "\nAuthor:", edit_new_author)

    # def search_books(self):
    # search_data = self.book_name
    # search_b = re.findall("/D", search_data)
    # print(search_b)
    def check_book_availability(self):
        print("Availablilty of books")
        print("========================")
        print("Halfgirlfriend not available")
        print("olivertwist available")


class Borrow_Returing_books(User):

    def __init__(self, borrow_books, return_books, id, name):
        super().__init__(id, name)
        self.borrow_books = borrow_books
        self.return_books = return_books

    def allow_users_borrow(self):
        print("register for borrowing book")
        print("================================")
        user_borrow=input("please enter your name:")
        user_book=input("please enter the name of your book:")
        print(user_borrow,"has borrowed the book",user_book)
        if __name__ == "__main__":
            notification.notify(
                title="You can borrow the book",
                message="hi user you must return the book within 15 days",
                timeout=3
            )
        time.sleep(10)

    def borrow_return(self):
        user_name = self.name
        print("Track Books")
        print(user_name, "Borrowed Book on", self.borrow_books, "And returned on", self.return_books)




class Management(User):
    def __init__(self, id, name):
        super().__init__(id, name)

    def result(self):
        print("Reservation of book")
        print("=========================")
        print(self.name, "reserved the book Halfgirlfriend")
        if __name__ == "__main__":
            notification.notify(
                title="Book reserved",
                message="hi your book is reserved",
                timeout=3
            )
        time.sleep(10)


class Fine:

    def fine_book(self):
        global charge
        print("Fines charged:")
        print("=======================")
        number_of_days = int(input("Enter the number of days:"))

        if 0 < number_of_days <= 5:
            charge = 2 * number_of_days

        charge_of_5days = 2 * 5
        if 5 < number_of_days <= 10:
            charge = charge_of_5days + (number_of_days - 5) * 2

        charge_of_10days = charge_of_5days + (number_of_days - 5) * 2
        if 10 < number_of_days <= 15:
            charge = charge_of_10days + (number_of_days - 10) * 2
        print(f"The fine charge is {charge}")

    def pay_fine(self):


        if __name__ == "__main__":
            notification.notify(
                title="PAY FINE",
                message="hi user please pay your fine",
                timeout=3
            )
        time.sleep(10)


class Reporting():
    def __init__(self,id,name,borrow_books,return_books):
        self.id=id
        self.name=name
        self.borrow_books=borrow_books
        self.return_books=return_books




    def reporting_user(self):
        print("User details")
        print("================")
        print(self.name, "[Id:", self.id, "]")
        print("Borrowed book on ", self.borrow_books, "and retured on", self.return_books)




# user

user_obj = User("5455", "Anu")
user_obj1 = User("5698", "Neetha")
user_obj2 = User("5869", "Anju")
user_obj.add_new_users()
user_obj1.add_new_users()
user_obj2.add_new_users()

# edit

user_obj.edit("anjali")
user_obj1.edit("ram")
user_obj2.edit("rahul")

# delete

# user_obj1.delete()

# Book

book_obj = Book("Oliver Twist", "Charles Dickens")
book_obj1 = Book("Half Girlfriend", "Chettan Baghat")
book_obj.add_new_book()
book_obj1.add_new_book()
# edit
book_obj.edit_book("Discovery of India", "Thomas Hardy")
# search
# book_obj.search_books()

book_obj.check_book_availability()

# Borrow and return

b_r_obj = Borrow_Returing_books("12 feb 2022", "25 march 2022", "255", "Anu")
b_r_obj.borrow_return()
b_r_obj.allow_users_borrow()

# Management
management_obj = Management("555", "Anu")
management_obj.result()

# fine
fine_obj = Fine()
fine_obj.fine_book()
fine_obj.pay_fine()

# Reporting

report_obj = Reporting("456","Anu","12 march 2023","25 march 2023")
report_obj.reporting_user()
