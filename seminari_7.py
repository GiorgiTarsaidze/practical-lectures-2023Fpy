# 1. In a file named "palindrome.py," create a program that prompts the
# user for a word or phrase and checks if it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and letter casing).
# Output "True" if it's a palindrome, and "False" if it's not.

# 2. In a file named "calculator.py," implement a basic calculator program that allows
# the user to perform addition, subtraction, multiplication, and division on two numbers.
# Prompt the user for the operation they want to perform, and then for the two numbers
# to operate on. Output the result of the operation.


# 1 შექმენით ლექსიკონი, სადაც ჩაიწერება სტუდენტის ქულები სხვადასხვა საგნებში.
# გამოიტანეთ შესაბამისი საგნების ქულები .items() მეთოდით.

# student_sandro = {
#     "Math": 90,
#     "History": 80,
#     "English": 78,
#     "Georgian": 98
# }
# student_giorgi = {
#     "Math": 78,
#     "History": 98,
#     "English": 80,
#     "Georgian": 93
# }

# names = ["Sandro", "Giorgi", "Mariami", "Dato"]
#          0          1         2         3

# students = {
#     'student_sandro' : {"Math": 90, "History": 80, "English": 78, "Georgian": 98},
#     'student_giorgi' : {"Math": 78, "History": 98, "English": 80, "Georgian": 93}
# }

# print(students["student_sandro"]["History"])



# 2 ნაძვის ხე:
# შექმენით პროგრამა, რომელიც დაბეჭდავს 'ნაძვის ხეს', რომლის
# სტრიქონების (სიმაღლის) რაოდენობა დამოკიდებული იქნება მომხარებლის ინფუთზე.
# ანუ თუ იუზერი ინფუთად შეიყვანს 5-ს, მაშინ უნდა გამოიბეჭდოს ასეთი ნაძვის ხე:
#     *
#    ***
#   *****
#  *******
# *********
#     |

# docstrings
'''
rows = int(input("Enter number of rows in the Christmas tree: "))

# rows = 5
# 0,1,2,3,4

for element in range(rows):
    spaces = " " * (rows - element - 1)
    # spaces = "  "
    snowflake = "*" * (element * 2 + 1)
    # snowflake = "*****"
    print(spaces + snowflake)
    # "  *****"

print(" " * (rows - 1)+"|")
'''


# 3 Vending Machine:
# ჩათვალეთ რომ სნექების აპარატში, ჩიფსები ღირის 50 ცენტი. შექმენით ამ აპარატის პროტოტიპი,
# რომელიც იღებს მხოლოდ 1,5,10, 25 ცენტიან მონეტებს და იქამდე გეკითხებათ ინფუთის შეყვანას,
# სანამ 50 ცენტს სრულად არ ამოწურავთ. გააკეთეთ ინფუთის ვალიდაცია.



# მაგალითი:
# Insert a coin (1, 5, 10, or 25 cents): 10
# Amount due: 40 cents
# Insert a coin (1, 5, 10, or 25 cents): 5
# Amount due: 35 cents
# Insert a coin (1, 5, 10, or 25 cents): 3
# Invalid coin denomination. Ignored.
# Insert a coin (1, 5, 10, or 25 cents): 25
# Amount due: 10 cents
# 25
# Change owed: 15 cents

chips = 50

accepted_coins = [1, 5, 10, 25]

while chips > 0:
    print(f"Amount due: {chips}")
    ask = int(input("Insert a coin (1, 5, 10, or 25 cents): "))
    if ask in accepted_coins:
        # chips = chips - ask
        chips -= ask
    else:
        print("Invalid coin denomination. Ignored.")

print(f"Change owned: {abs(chips)}")

print("Here you go! Take it!")
