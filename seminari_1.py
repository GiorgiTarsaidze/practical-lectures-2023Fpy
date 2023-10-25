# 1 შეეკითხეთ იუზერს input-ით სახელი და შემდეგ მიესალმეთ მას fstring-ების გამოყენებით

# name = input("Whats your name? ")
# print(f"Hello {name}")


# 2 შექმენით ფუნქცია, რომელიც ითვლის ორი რიცხვის ჯამს

# num_1 = int(input("First number: "))
# num_2 = int(input("Second number: "))

# def jami(num_1,num_2):
#     return(num_1+num_2)

# print(jami(num_1,num_2))

# 3 შექმენით ფუნქცია, რომელიც ითვლის ორი რიცხვის ნამრავლს

# num_1 = int(input("First number: "))
# num_2 = int(input("Second number: "))

# def namravli(num_1,num_2):
#     return num_1 * num_2

# print(namravli(num_1, num_2))


# 4 შექმენით ფუნქცია, რომელიც ითვლის რიცხვის კვადრატს

# number = int(input("Number: "))

# def kvadrati(number):
#     return number*number

# ricxvis_kvadrati = kvadrati(number)
# print(ricxvis_kvadrati)


# 5 ფუნქცია, რომელიც ითვლის მართკუთხედის ფართობს და პერიმეტრს

# gverdi_1 = int(input("გვერდი 1: "))
# gverdi_2 = int(input("გვერდი 2: "))

# def area(gverdi_1,gverdi_2):
#     fartobi = gverdi_1 * gverdi_2
#     perimetri = 2*(gverdi_1+gverdi_2)

#     return fartobi,perimetri


# fartobi, perimetri = area(gverdi_1, gverdi_2)

# print(f"მართკუთხედის ფართობია: {fartobi} სმ ")
# print(f"მართკუთხედის პერიმეტრია: {perimetri} სმ")

# 6 input-ის გამოყენებით სთხოვეთ იუზერს ორი რიცხვის შეყვანა და გამოთვალეთ მათი
# დამრგვალებული განაყოფი

# number_1 = int(input("first: "))
# number_2 = int(input("second: "))

# def calculator(number_1,number_2):
#     return round(number_1/number_2)

# print(calculator(number_1,number_2))

# 7 შექმენით ფუნქცია, რომელიც დაითვლის ორი რიცხვის საშუალო არითმეტიკულს

# number_1 = int(input("first: "))
# number_2 = int(input("second: "))

# def sashualo(number_1,number_2):
#     return (number_1+number_2)/2

# print(sashualo(number_1,number_2))



# 8 ფუქნცია, რომელიც დაითვლის გადაცემული სტრინგის სიმბოლოების ზომას

# word = input("your word: ")

# def length(word):
#     return len(word.strip())

# print(length(word))


# 9 მისალმების ფუნქცია ნაგულისხმევი პარამეტრით

# name = input("Whats your name? ")

# def hello(name="Unknown"):
#     print(f"Hello {name}!")

# hello(name)


# 10 დაითვალეთ ორი რიცხვის განაყოფის ნაშთი

# num_1 = int(input("პირველი: "))
# num_2 = int(input("მეორე: "))

# print(num_1%num_2)
