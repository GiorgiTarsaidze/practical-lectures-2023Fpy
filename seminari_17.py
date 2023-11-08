
# 1
# Read a CSV file containing student information (name, age, grade) and display the contents.
# Print each student's information in a structured manner.

# import csv
# from tabulate import tabulate

# student_data = []

# with open("data_1.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         student_data.append(row)

# print(tabulate(student_data))



# 2
# Create a program that takes user input for a new student's information (name, age, grade).
# Append this information to an existing CSV file containing student records.
# import csv
# from tabulate import tabulate

# name = input("Whats your name? ")
# age = input("How old are you? ")
# grade = input("Whats your average grade? ")

# student_data = []

# with open("data_1.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,age,grade])
#     writer.writerow(["Lasha","20","B"])

# with open("data_1.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         student_data.append(row)

# print(tabulate(student_data))







# 3
# Read a CSV file with columns 'Product', 'Price', 'Quantity'.
# Calculate the total cost for each product (Price * Quantity) and create a new CSV file with Product and Total Cost columns.
# import csv

# with open("data_3.csv", "r") as file:
#     reader = csv.DictReader(file)
#     new_rows = []
#     final_list = []


#     for row in reader:
#         total_sum = int(row["Price"]) * int(row["Quantity"])
#         row["Total Cost"] = total_sum
#         new_rows.append(row)


#     for element in new_rows:
#         element.pop("Price")
#         element.pop("Quantity")
#         final_list.append(element)

# with open("cost_after.csv", "w") as file:
#     fieldnames = ["Product","Total Cost"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(final_list)





# 4
# Read a CSV file with columns 'ID', 'Name', 'Age'.
# Prompt the user to enter an age. Display all records of individuals with that age.

import csv
from tabulate import tabulate

age = input("Enter the age you want to find: ")

my_list = []

with open("data_4.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Age"] == age:
            my_list.append(row)

print(tabulate(my_list, headers ="keys"))















# Read a CSV file containing 'Name' and 'Score' columns.
# Sort the records by 'Score' in descending order and write them to a new CSV file.


# Read a CSV file containing 'Country', 'Population', 'Area'.
# Calculate the population density (Population / Area) for each country and append this information to the existing CSV file.
