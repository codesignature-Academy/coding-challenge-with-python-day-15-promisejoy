class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        else:
            print(f"Sorry, '{book.title}' is already borrowed")
            return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        else:
            print(f"{self.name} doesn't have '{book.title}' borrowed")
            return False
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - Books borrowed: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}'")
    
    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")
    
    def show_available_books(self):
        print("\n--- Available Books ---")
        available_books = [book for book in self.books if not book.is_borrowed]
        if available_books:
            for book in available_books:
                print(f"  - {book}")
        else:
            print("  No available books")
        print()
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

def main():
    library = Library()
    
    print(" BOOKS IN THE LIBRARY ")
    book1 = Book("Introduction To Python", "SmartDev", "#12345")
    book2 = Book("Python Crash Course", "SmartDev", "#67890")
    book3 = Book("Funtions In Python", "SmartDev", "#11223")
    book4 = Book("Classes In Python", "JSmartDev", "#44556")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    print("\n LIBRARY MEMBERS ")
    member1 = Member("Prospect", "1122")
    member2 = Member("SmartDev", "1133")
    member3 = Member("Rejoice", "1144")
    
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    
    library.show_available_books()
    
    print("\nBORROWING BOOKS")
    member1.borrow(book1)
    member1.borrow(book2)
    
    library.show_available_books()
    
    print("\nATTEMPTING TO BORROW BORROWED BOOK")
    member2.borrow(book1)
    
    member2.borrow(book3)
    
    library.show_available_books()
    
    print("\n RETURNING BOOKS ")
    member1.return_book(book1)
    
    library.show_available_books()
    
    print("\nBORROWING RETURNED BOOK")
    member3.borrow(book1)
    
    library.show_available_books()
    
    print("\nMEMBER STATUS")
    print(member1)
    print(member2)
    print(member3)

if __name__ == "__main__":
    main()