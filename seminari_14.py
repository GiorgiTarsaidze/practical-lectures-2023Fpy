# def main():
#     first_num = int(input("First number: "))
#     second_num = int(input("Second number: "))

#     operation = input("Choose operation [+,-,*,/]: ")

#     if operation == "+":
#         print(add(first_num, second_num))
#     elif operation == "-":
#         print(subtract(first_num, second_num))
#     elif operation == "*":
#         print(multiply(first_num, second_num))
#     else:
#         # if second_num == 0:
#         #     print("Second number cant be zero")
#         # else:
#         print(divide(first_num, second_num))


# def add(a,b):
#     return a + b

# def subtract(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# def divide(a,b):
#     return a / b

# if __name__ == "__main__":
#     main()



def main():
    print("1. Count vowels")
    print("2. Reverse String")
    print("3. Is palindrome")
    number = input("Which operation do we need? ")

    possible_nums = ["1","2","3"]
    if number in possible_nums:
        text = input("What's your string? ").lower()

        if number == "1":
            print(count_vowel(text))
        elif number == "2":
            print(reverse_string(text))
        else:
            print(palindrome(text))
    else:
        print("Choose only 1, 2 or 3")

def count_vowel(text):
    # text = "banana"
    vowels = "aeiou"
    counter = 0

    for element in text:
        if element in vowels:
            counter += 1
    return counter

def reverse_string(text):
    reversed_string = text[::-1]
    return reversed_string

def palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    main()


# text = "banana"

# print(text[::-1])
