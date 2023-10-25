# სავარჯიშო 1 - username წმენდა:
# შექმენით პროგრამა,რომელიც შეამოწმებს მომხარებლის username-ს შემდეგი პირობები:

# შეამოწმეთ, თუ მომხმარებლის სახელი სიმბოლოების სიგრძე აღემატება 6-ს. თუ აღემატება, მაშინ გამოიტანეთ რომ სახელი ვალიდურია
# თუ იგი შეიცავს სფეისებს ან 6 სიმბოლოზე ნაკლებს, მაშინ გამოიტანეთ შეტყობინება, რომ ვალიდური არ არის.
# სანამ ამ ყველაფერს იზამთ, მოაშორეთ ზედმეტი სფეისები ინფუთიდან


# def main():
#     username = input("Whats your username? ").strip()
#     validated_name = length_validator(username)

#     if validated_name:
#         print("Your username is valid!")
#     else:
#         print("Your username is not valid!")

# def length_validator(username):
#     length = len(username)
#     if length < 6 or " " in username:
#         return False
#     else:
#         return True

# main()










# სავარჯიშო 2 - პაროლის შემოწმება:
# შექმენით პროგრამა, რომლითაც შეამოწმებთ პაროლის სიძლიერეს.

# any(char.isdigit() for char in x):

# პირობები:
# პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო
# პაროლი უნდა შეიცავდეს 1 uppercase სიმბოლოს მინიმუმ
# პაროლი უნდა შეიცავდეს 1 lowercase სიმბოლოს მინიმუმ
# პაროლი უნდა შეიცავდეს მინიმუმ 1 ციფრს.
# პაროლი არ უნდა იყოს სიტყვა 'password' -ს

def main():
    username = input("Whats your name? ").strip()
    password = password_validator(input("Whats your password? ").strip())

    if password:
        print(f"{username.title()}, your password is strong!")
    else:
        print(f"{username.title()}, your password is weak!")


def password_validator(password):
    length = len(password)

    if length >= 8:
        if password.lower() != "password":
            if password.lower() != password:
                if password.upper() != password:
                    if not password.isalpha():
                        return True
    return False

main()


