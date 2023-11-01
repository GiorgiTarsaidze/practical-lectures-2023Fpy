books = {
    "Topuria": ["Math", "fsf"],
    "Franz Kafka": "Gardasaxva",
}

def main():
    while True:
        print("1. View books")
        print("2. Add book")
        print("3. Remove book")
        print("4. Search book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for element in view_books():
                print(element)
        elif choice == "2":
            author = input("Enter new author: ").strip()
            book = input("Enter new book: ").strip()

            if add_book(author,book):
                print("Book added!")
        elif choice == "3":
            author = input("Enter author your want to remove: ").strip()
            if remove_book(author):
                print("Book successfully removed!")
            else:
                print("Book not found in library.")
        elif choice == "4":
            book = input("Enter book: ").strip()
            if search_book(book):
                print("Book Available in our library!")
            else:
                print("Book not found!")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")



def view_books():
    sorted_books = []
    for key, values in books.items():
        if isinstance(values,str):
            sorted_books.append(f"{key} - {values}")
        else:
            sorted_books.append(f"{key} - {', '.join(values)}")
    return str(sorted_books)

def add_book(author,book):
    # 1
    # if author in books and isinstance(books[author], list):
    #     books[author].append(book)
    # elif author in books and isinstance(books[author], str):
    #     books[author] = books[author].split()
    #     books[author].append(book)
    #     # books[author] = book # list
    # else:
    #     books[author] = book
    # print(books)

    # 2
    try:
        books[author].append(book)
    except KeyError:
        books[author] = book
    except AttributeError:
        simple_list = []
        simple_list.append(books[author])
        simple_list.append(book)
        books[author] = simple_list

    return True

def remove_book(author):
    if author in books:
        books.pop(author)
        return True
    return False
    # კონკრეტული წიგნი წასაშლელი <-

def search_book(book):
    # dict_values = books.values()

    # ჩასამატებელი მაგალთად 'ga' -ზე მაინც True-ს აბრუნებს
    for element in books:
        if book in books[element]:
            return True
    return False

if __name__ == "__main__":
    main()

# my_list = []

# print(isinstance(my_list, list))


# ragaca_stringi = "wowwo wwow"

# print(ragaca_stringi.split(" "))
