# name = input("Whats your name?")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# file.write - ჩაწერა ახალი მონაცემის
# .readlines() - ხაზების წაკითხვა
# csv - comma seperated value

# names = []

# with open("names.txt", "r") as file:
#     # lines = file.readlines()
#     for line in file:
#         names.append(line.rstrip())


# for element in sorted(names):
#     print(element)

# Giorgi,Bitcamp,19      my_list = line.split(",")  row = ["Giorgi", "Bitcamp", "19"]

# import csv

# students = []

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"], "company":row["company"]})
    # for row in reader:
    #     students.append({"name":row[0],"company":row[1]})

    # for line in file:
    #     name,company = line.rstrip().split(",")
    #     student = {"name":name,"company":company}
    #     students.append(student)


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} works at {student['company']}")



# import csv

# name = input("Whats your name? ")
# company = input("Where do you work at? ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "company"])
#     writer.writerow({"name": name, "company": company})


# Pillow - PIL

# name = input("Whats your name? ")

# file = open("hello.txt", "a")
# file.write(name)
# file.close()


with open("hello.txt", "r") as file:
    for row in file:
        print(row.rstrip())

