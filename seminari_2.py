# 1. ასაკის შეზღუდვა

# def main():
#     get_age = get_input()
#     print(regulator(get_age))


# def get_input():
#     age = int(input("Whats your age? "))
#     return age

# def regulator(age):
#     if age <= 18:
#         return "You cant watch this movie!"
#     elif age > 18 and age < 25:
#         return("Its okay! ")
#     else:
#         return("You are allowed to watch this movie!")

# main()


# 2. თუ ცვლადი = საძიებელ რიცხვს

# number = 12

# get_number = int(input("Whats your number: "))

# if get_number > number:
#     print("Your number is higher!")
# elif get_number < number:
#     print("Your number is lower!")
# elif get_number == number:
#     print("Thats your number!")
# else:
#     print("wrong input!")


# 3. თუ სტრინგი არის საძიებელ სტრინგში

# sentance = "John went to school"

# if "432142" in sentance:
#     print(" is in sentance!")
# else:
#     print("No")






# 4. ქულების შესამოსმებელი კოდი

# number = int(input("Whats your score? "))

# if number > 100:
#     print("Not a real grade")
# elif number >= 90 and number <= 100:
#     print("Your grade is A")
# elif number < 90 and number >= 80:
#     print("Your grade is B")
# elif number < 80 and number >= 70:
#     print("Your grade is C")
# elif number < 70 and number >= 60:
#     print("Your grade is D")
# elif number < 60 and number >= 50:
#     print("Your grade is E")
# else:
#     print("Your grade is F, you did not pass!")

# 5. ლუწი თუ კენტი


def main():
    number = get_input()
    even_or_odd(number)

def get_input():
    number = int(input("Whats your number? "))
    return number

def even_or_odd(number):
    if number == 0:
        print(f"{number} 0-ია")
    elif number % 2 == 0:
        print(f"{number} ლუწია")
    else:
        print(f"{number} კენტია")

main()
