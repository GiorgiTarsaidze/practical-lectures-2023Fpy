'''
4. შექმენით პროგრამა, რომელსაც მოაქვს ინფორმაცია github-ის რეპოზიტორების შესახებ
'''

# raise <- ერორის 'გამოძახება'
# import math

# def main():
#     number = get_input()
#     squared_number = math.sqrt(number)

#     print(f"Square root of {number} is {squared_number}.")

# def get_input():
#     while True:
#         try:
#             number = float(input("Enter your number: "))
#             if number < 0:
#                 raise KeyError
#             return number
#         except ValueError:
#             continue

# if __name__ == "__main__":
#     main()

# import math

# def main():
#     radius = get_input()
#     print(f"Area of your circle is: {area_calculator(radius)}")

# def get_input():
#     while True:
#         try:
#             radius = float(input("Enter your radius: "))
#             if radius <= 0:
#                 raise ValueError
#             return radius
#         except ValueError:
#             continue

# def area_calculator(radius):
#     area = math.pi * math.pow(radius,2)
#     return area

# if __name__ == "__main__":
#     main()

# area = pi * r **2


'''
4. შექმენით პროგრამა, რომელსაც მოაქვს ინფორმაცია github-ის რეპოზიტორების შესახებ
'''

# API

# https://api.github.com/repos/dmalan/cybersecurity
# https://api.github.com/repos/{owner}/{repository}

import requests

owner = input("Github owner username: ")
repository = input("repository name: ")


url = f"https://api.github.com/repos/{owner}/{repository}"


response = requests.get(url)

data = response.json()

id = data["id"]
network_count = data["network_count"]
forks = data["forks"]
size = data["size"]
owner = data["owner"]["login"]

print(forks)
print(size)
print(network_count)
print(owner)
print(f"id: {id}")

