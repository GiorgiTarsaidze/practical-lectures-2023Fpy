# docstring
# identation - 4 სფეისი, ბიჯით გადაწევა

'''
1. შექმენით პროგრამა, რომელიც დაითვლის მართკუთხედის ფართობს.
კოდი, command-line argument-ების მეშვეობით მიიღებს ორ არგუმენტს, სიგრძესა და სიგანეს.
ამის შემდეგ დაითვლის მართუკუთხედის ფართობს. გააკეთეთ შესაბამისი ვალიდაციები და შეფუთეთ
კოდი ფუნქციებად
'''

# import sys

# def main():
#     if len(sys.argv) == 3:
#         try:
#             length = float(sys.argv[1])
#             width = float(sys.argv[2])
#             print(f"Area of your rectangle: {calculate_rectangle_area(length,width)}")
#         except ValueError:
#             print("Invalid input. Length and width must be numbers.")
#     else:
#         print("Enter length and width command-line arguments only!")

# def calculate_rectangle_area(length, width):
#     area = length * width
#     return area


# if __name__ == "__main__":
#     main()


'''
2. შექმენით პროგრამა, რომელიც დაითვლის დღეების სხვაობას ორ შეყვანილ
თარიღს შორის. გააკეთეთ ვალიდაციები, შეფუთეთ კოდი ფუნქციებად.
'''

# 25-10-2023
# 20-07-2021
# 5 days
# datetime

# import datetime

# def main():
#     date1 = input("Enter the first date (YYYY-MM-DD) ")
#     date2 = input("Enter the second date (YYYY-MM-DD) ")

#     print(f"Days: {days_between_calculator(date1, date2)}")

# def days_between_calculator(date1, date2):
#     try:
#         date_1 = datetime.datetime.strptime(date1, "%Y/%m/%d")
#         date_2 = datetime.datetime.strptime(date2, "%Y/%m/%d")
#         print(date_1)
#         print(date_2)
#         result = date_1 - date_2
#     except ValueError:
#         print("Invalid input!")

#     return result.days


# if __name__ == "__main__":
#     main()








'''
3. შექმენით ხუმრობების გენერატორი კოდი. (pyjokes)
'''

# import pyjokes

# def main():
#     print(joke_generator())

# def joke_generator():
#     joke = pyjokes.get_joke()
#     return joke

# if __name__ == "__main__":
#     main()


'''
4. შექმენით პროგრამა, რომელსაც მოაქვს ინფორმაცია github-ის რეპოზიტორების შესახებ
'''




'''
5. წამოიღეთ ინფორმაცია ამ API-დან https://www.boredapi.com/api/activity. დაახარისხეთ
ინფორმაცია და გამოიტანეთ შესაბამისად. გააკეთეთ ვალიდაციები.
'''
import requests

url = "https://www.boredapi.com/api/activity"

response = requests.get(url)


activity_data = response.json()
print(activity_data["activity"])
print(activity_data["type"])
