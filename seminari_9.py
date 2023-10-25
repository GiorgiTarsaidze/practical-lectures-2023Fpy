# 1. შექმენით რიცხვების ლისტი. შეეკითხეთ მომხარებელს თუ რომელი ინდექსის
# შესაბამისი ელემენტი უნდა რომ გამოიტანოს. თუ ეს ინდექსი არ არსებობს,
# გამოიტანეთ შესაბამისი შეტყობინება.


# my_list = [1,2,3,4,5]
# #          0 1 2 3 4
# try:
#     index_input = int(input("Whats the index? "))
#     print(f"Value at index {index_input} is {my_list[index_input]}")
# except IndexError:
#     print("Your index is out of range!")
# except ValueError:
#     print("Invalid input!")

# --------------------------

# 2. შექმენით ლექსიკონი, რომელშიც აღწერთ კონკრეტულ ადამიანს სახელით, ასაკითა და
# საცხოვრებელი ადგილით. ეცადეთ გამოიტანოთ ისეთი გასაღები, რომელიც არ გაქვთ განსაზღვრული.
# გააკეთეთ ვალიდაცია.

# json
# person = {
#     "name": "Sandro",
#     "age":25,
#     "city":"Tbilisi",
#     "courses": {
#         "Math": 98,
#         "Python": 78,
#         "English": 45
#     }
# }

# print(person["courses"]["Math"])

# try:
#     key = input("Whats the key? ")
#     print(person[key])
# except KeyError:
#     print("Your key was not found in the dictionary!")



# 3. შექმენით პროგრამა, რომელიც მომხარებელს input-ში რაიმე რიცხვს ეკითხება 5-ჯერ, მიყოლებით.
# გააკეთეთ ნებისმიერი სახის ვალიდაცია, რაც კი შეიძლება ამ პროცესის დროს მოხდეს.
# პროგრამამ საბოლოოდ უნდა გამოიტანოს ამ 5 რიცხვის ჯამი.

# sum = 0
# for element in range(5):
#     while True:
#         try:
#             num = int(input("Enter the number: "))
#             sum += num
#             break
#         except ValueError:
#             print("Error, invalid input!")

# print(sum)












# 4. შექმენით ლისტი ელემენტებით. შეეკითხეთ მომხარებელს ინდექსის input-ი და სცადეთ რომ
# მიწვდეთ შესაბამისი ინდექსის ელემენტს. თუ მომხმარებელი შეიყვანს უარყოფით რიცხვს,
# დაასრულეთ პროგრამის მუშაობა და გამოიტანეთ საბოლოო სახის ლისტი. თუ მომხარებელი შიეყვანს
# ინდექსს, რომელიც არ არის თქვენს ლისტში, შეეკითხეთ მომხმარებელს ახალი ელემენტის დამატების
# input-ი და დაამატეთ ეს ახალი ელემენტი.(გააკეთეთ ეს შესაბამისი ერორის დაჭერით).
# ეს პროცესი იქამდე უნდა ხდებოდეს, სანამ მომხარებელი არ შიეყვანს უარყოფით რიცხვს თავდაპირველ
# ინფუთში

# names = ["Luka", "Giorgi", "Oto", "Mariami", "Nini", "Sandro"]
# #          0       1         2       3         4        5

# while True:
#     try:
#         index_input = int(input("Whats the index? "))

#         if index_input < 0:
#             break
#         print(names[index_input])
#     except IndexError:
#         print("That value does not exist!")
#         new_element = input("Enter the new element: ")
#         names.append(new_element)
#         print("I added your element")
#     except ValueError:
#         print("Incorrect value! Try Again!")

# print(names)





# 5. შექმენით სტუდენტების ქულების მენეჯმენტის პროგრამა.
# შექმენით ცარიელი ლექსიკონი, სადაც სტუდენტების ქულები ჩიაწერება.
# შექმენით მარტივი მენიუს სისტემა, სადაც მომხარებელს შეუძლია აირჩიოს ქმედება. მაგალითად:
'''
Student Grade Management System
--------------------------------
1. Add a new student and their grades
2. Display the grades for a specific student
3. Calculate the average grade for a student
4. List all students and their grades
5. Quit

Enter your choice:
'''
# როცა ახალ სტუდენტს დაამტებთ, გააკეთეთ ვალიდაცია exception-ების გამოყენებით.
# გააკეთეთ ვალიდაცია, თუ ვერ იპოვით შესაბამის სტუდენტს.
# მეოთხე ვარიანტის დროს, მწკრივში გამოიტანეთ ყველა სტუდენტი

student_grades = {'Sandro': ['67', '92', '47'], 'Giorgi': ['56','99','100']}

def main():
    while True:
        print("\nStudent Grade Management System")
        print("--------------------------------")
        print("1. Add a new student and their grades")
        print("2. Display the grades for a specific student")
        print("3. Calculate the average grade for a student")
        print("4. List all students and their grades")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_grade()
        elif choice == "2":
            display_grades()
        elif choice == "3":
            average_calculator()
        elif choice == "4":
            list_students()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def add_student_grade():
    name = input("Enter student's name: ")
    grades_str = input("Enter student's grades: ").split(",")
    # grades = []
    # for element in grades_str:
    #     try:
    #         grade = int(element)
    #         grades.append(grade)
    #     except ValueError:
    #         print("Invalid grade!")

    student_grades[name] = grades_str
    print(student_grades)

def display_grades():
    try:
        name = input("Enter student's name: ")
        print(name + " Grades: " + ", ".join(student_grades[name]))
    except KeyError:
        print(f"{name} - no such student!")


def average_calculator():
    try:
        name = input("Enter student's name: ")
        grades = student_grades[name]
        grades_length = len(grades)

        sum = 0
        for element in grades:
            element = int(element)
            sum += element

        print(f"Average grade is {round(sum / grades_length)} points.")

    except KeyError:
        print(f"{name} - no such student!")

def list_students():
    for names, grades in student_grades.items():
        print(f"{names} : " + ", ".join(grades))

main()
