import json
def readlib():
    try:
        with open("library.json","r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        with open("library.json","w") as f:
            json.dump([], f)
        return []

def savelib(info):
    with open("library.json","w") as f:
        json.dump(info, f, indent=2)


class Library:
    def __init__(self):
        self.library = readlib()

    def add_book(self, bkname, author, code, status = "Available"):
        
        for book in self.library:
            if book["Code"]==code:
                print("Book code already exists.")
                return

        bkdata = {
            "Name":bkname,
            "Author":author,
            "Code":code,
            "Status":status
        }
        self.library.append(bkdata)
        savelib(self.library)
        print("Book added.")

    def remove_book(self, code):
        book = self.find_book(code)
        if book is None:
            print("Book not found.")
            return
        
        if book["Status"] == "Borrowed":
            print("Book is currently borrowed.")
            return

        self.library.remove(book)
        savelib(self.library)
        print("Book removed.")
        


    def search_book(self, code):
        
        book = self.find_book(code)
        if book is None:
            print("Book not found.")
        else:
            self.display_book(book)

    def display_all(self):
        
        if not self.library:
            print("No Book in Library.")
            return
        
        for book in self.library:
            self.display_book(book)

    def display_avail(self):
        
        found = False
        for book in self.library:
            if book["Status"] == "Available":
                found = True
                self.display_book(book)
        if not found:
            print("No book available.")
            return

    def book_count(self):
        
        if not self.library:
            print("No book in library.")
            return

        available_book = 0
        borrowed_book = 0
        for book in self.library:
            if book["Status"] == "Available":
                available_book += 1
            elif book["Status"] == "Borrowed":
                borrowed_book += 1

        print("Total Book :",len(self.library))
        print("Available Book :",available_book)
        print("Borrowed Book :",borrowed_book)


    def borrow_book(self, code):  
        book = self.find_book(code)

        if book is None:
            print("Book not found.")
            return
        
        if book["Status"] == "Borrowed":
            print("Book is already borrowed.") 
            return   
        
        book["Status"]="Borrowed"
        print("Book borrowed.")
        savelib(self.library)

    def return_book(self, code):
        book = self.find_book(code)
        if book is None:
                print("Book not found.")
                return
        if book["Status"] == "Available" :
            print("Book is already available.")
            return
           
        book["Status"] = "Available"
        print("Book returned.")
        savelib(self.library)

    def display_book(self, book):
        print("-------------------------------------")
        print("Code:",book["Code"])
        print("Name:",book["Name"])
        print("Author:",book["Author"])
        print("Status:",book["Status"])
        print("-------------------------------------")

    def update_book(self, code):
        book = self.find_book(code)
        if book is None:
                print("Book not found.")
                return
        
        changed = False
        while True:
            print("1.Change Name")
            print("2.Change Author")
            print("3.Cancel")

            try:
                option = int(input("Enter associated number of your choice :"))
                if option == 1:
                    change_name = input("Enter New Name :")
                    book["Name"] = change_name
                    print("Name successfully changed.")
                    changed = True
                    

                elif option == 2:
                    change_author = input("Enter New Author :")
                    book["Author"] = change_author
                    print("Author successfully changed.")
                    changed = True

                elif option == 3:
                    print("Update cancelled.")
                    break
                else:
                    print("Incorrect value entered.")
        
            except ValueError:
                print("Please input correct choice.")
    
        if changed:
            savelib(self.library)
        else:
            print("No change made.")

    def find_book(self, code):
        for book in self.library:
            if book["Code"] == code:
                return book
        return None
 
        
            

                 
             


def get_code():
    return input("Enter Book Code :").strip().upper()
lib = Library()       
print("Welcome to XYZ Library.")
ask = input("Do you want to continue ? :")

if ask.lower() == "yes":
    while True:
        print("\n"+"MENU")
        print("--------------------")
        print("1.ADD BOOK")
        print("2.REMOVE BOOK")
        print("3.BORROW BOOK")
        print("4.RETURN BOOK")
        print("5.SEARCH BOOK")
        print("6.DISPLAY ALL BOOKS")
        print("7.DISPLAY AVAILABLE BOOKS")
        print("8.BOOK COUNT")
        print("9.UPDATE BOOK")
        print("10.Exit")
        print("--------------------")
        try:
            option = int(input("Enter associated number of your choice :"))

           
            if option == 1:
                bk_code = get_code()
                bk_name = input("Enter book name:")
                bk_author = input("Enter the author name :")
                lib.add_book(bk_name, bk_author, bk_code)

            elif option == 2:
                bk_code = get_code()
                lib.remove_book(bk_code)

            elif option == 3:
                bor_book = get_code()
                lib.borrow_book(bor_book)

            elif option == 4:
                ret_book = get_code()
                lib.return_book(ret_book) 

            elif option == 5:
                book = get_code()
                lib.search_book(book)

            elif option == 6:
                lib.display_all()

            elif option == 7:
                lib.display_avail()

            elif option == 8:
                lib.book_count()

            elif option == 9:
                bk_code = get_code()
                lib.update_book(bk_code)

            elif option == 10:
                ask = input("Do you want to exit ?(yes/no) :")
                if ask.lower() == "yes":
                    print("Have a nice day.")
                    break
                else:
                    print("Incorrect input, try again.")
            else:
                print("Please input correct choice.")
        except ValueError:
            print("Please input correct choice.")           
else:
    quit()
