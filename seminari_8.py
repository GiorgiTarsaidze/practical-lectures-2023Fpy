# 1. In a file named "palindrome.py," create a program that prompts the
# user for a word or phrase and checks if it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and letter casing).
# Output "True" if it's a palindrome, and "False" if it's not.

# 2. In a file named "calculator.py," implement a basic calculator program that allows
# the user to perform addition, subtraction, multiplication, and division on two numbers.
# Prompt the user for the operation they want to perform, and then for the two numbers
# to operate on. Output the result of the operation.



# def main():
#     operation = get_operation_input()
#     first_number, second_number = get_input()
#     try:
#         if operation == "+":
#             result = addition(first_number, second_number)
#         elif operation == "-":
#             result = subtraction(first_number, second_number)
#         elif operation == "*":
#             result = multiplication(first_number, second_number)
#         else:
#             result = division(first_number, second_number)

#         print(f"Result: {result}")
#     except ZeroDivisionError:
#         print("You can't divide by zero.")



# def get_operation_input():
#     operation_list = ['+','-','*','/']
#     while True:
#         operation = input("What do you want to do ('+','-','*','/'): ")
#         if operation in operation_list:
#             return operation
#         else:
#             print("Not a valid operation")


# def get_input():
#     while True:
#         try:
#             first_number = int(input("What's the first number? "))
#             second_number = int(input("What's the second number? "))
#         except ValueError:
#             print("Your number is not an integer! ")
#         else:
#             break
#     return first_number, second_number

# def addition(num_1, num_2):
#     return num_1 + num_2

# def subtraction(num_1, num_2):
#     return num_1 - num_2

# def multiplication(num_1, num_2):
#     return num_1 * num_2

# def division(num_1, num_2):
#     return num_1 / num_2

# main()


# shopping_cart = []

# while True:
#     try:
#         product = input("Your product: ")
#         shopping_cart.append(product)
#     except EOFError:
#         break
# print()
# print("Your shopping cart: ")
# for product in shopping_cart:
#     print(product)

# ctrl + d

try:
    number_1 = int(input("First number: "))
    number_2 = int(input("Second number: "))

    print(number_1/number_2)
except Exception:
    print("EXCEPTION!")
else:
    ...
finally:
    ...
