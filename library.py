
# class Library:
#     def __init__(self,books,floors, categories):
#         self.books = books
#         self.floors = floors
#         self.categories = categories


#     def __str__(self):
#         return f"{self.books} - {self.categories}"

#     def remove_book(self):
#         return f"{self.books}"

#     @staticmethod
#     def print_books(new_book):
#         print(new_book)

#     @classmethod
#     def sort_categories(cls, x):

#         # obj_2 = Library(["5","6","7"],1,["foasf", "Science"])
#         obj_2 = cls(["5","6","7"],1,["foasf", "Science"])

#         print(obj_2)


# obj_1 = Library(["1","2","3"], 2, ["Math", "Science", "Scifi"])

# obj_1.sort_categories(obj_1)






# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     @staticmethod
#     def get_max_value(x, y):
#         return max(x, y)

# # Create an instance of MyClass
# obj = MyClass(10)

# print(MyClass.get_max_value(20, 30))

# print(obj.get_max_value(20, 30))




class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_name, quantity):
        if not isinstance(book_name, str) or not isinstance(quantity,int):
            raise ValueError("Invalid input values!")

        self.books[book_name] = quantity

    @classmethod
    def from_existing_books(cls, existing_books):
        if not isinstance(existing_books, dict):
            raise ValueError("existing_books must be a dictionary!")

        library = cls()
        for book, quantity in existing_books.items():
            library.add_book(book, quantity)

        return library

    

    @staticmethod
    def is_valid(id):
        return id.isdigit() and (len(id)>=10 and len(id)<=15)

    def __str__(self):
        return f"{self.books}"




my_library = Library()


my_library.from_existing_books({"Python Basics":5, "OOP python":10, "Django":3})
print(my_library.books)

my_library.add_book("Python", 4)

print(my_library.books)
