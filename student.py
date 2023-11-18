# # # tuple
# # # instance, dunder



# # class Human:
# #     def __init__(self,name,company):
# #         if not name:
# #             raise ValueError("Missing name")

# #         if company not in ["Bitcamp", "Facebook", "Amazon"]:
# #             raise ValueError("Invalid company")

# #         self.name = name
# #         self.company = company

# #     def __str__(self):
# #         return f"{self.name} from {self.company}!"

# #     def position(self):
# #         if self.company == "Bitcamp":
# #             return "HELLO BITCAMP!"
# #         elif self.company == "Facebook":
# #             return "Hi, facebook!"
# #         elif self.company == "Amazon":
# #             return "Whats up, amazon?"
# #         else:
# #             return "Nothing here!"


# #     #getter
# #     @property
# #     def company(self):
# #         return self._company

# #     #setter
# #     @company.setter
# #     def company(self,company):
# #         if company not in ["Bitcamp", "Facebook", "Amazon"]:
# #             raise ValueError("Invalid company")
# #         self._company = company

# #     @property
# #     def name(self):
# #         return self.name

# #     @name.setter
# #     def name(self,name):
# #         if name not in ["Giorgi", "Lasha", "Oto"]:
# #             raise ValueError("Invalid Name")
# #         self._name = name




# # def main():
# #     human = get_human()
# #     human.name = "Mariami"
# #     print(human)

# # def get_human():
# #     # human = Human()
# #     name = input("Whats your name: ")
# #     company = input("Where do you work at: ")
# #     human = Human(name, company)
# #     return human


# # if __name__ == "__main__":
# #     main()
# # # name = Human(name="Giorgi", company="Bitcamp")
# # # name = 123

# # # print(type(name))


# # import random

# # class Generator:
# #     companies = ["Bitcamp", "Facebook", "Amazon"]

# #     @classmethod
# #     def sort(cls, name):
# #         print(name, "works at", random.choice(cls.companies))

# #     # def generate_naem(self):
# #     #     return ...

# #     # def ragacaragaca(self):
# #     #     return ...

# # company = Generator()
# # company.sort("Giorgi")

# class Human:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("MISSING NAME")
#         self.name = name


# class Student(Human):
#     def __init__(self,name,university):
#         super().__init__(name)
#         self.university = university

#     def __str__(self):
#         return f"{self.name} from {self.university}"

# class Professor(Human, Student):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject = subject

#     def __str__(self):
#         return f"{self.name} from {self.subject}"


# human = Human("Giorgi")
# student = Student(name=None, university="Harvard")
# professor = Professor("Lasha", "Math")

# print(student)


# class Bank:
#     def __init__(self, dollari=0, lari=0, tetri=0):
#         self.dollari = dollari
#         self.lari = lari
#         self.tetri = tetri

#     def __str__(self):
#         return f"{self.dollari} $, {self.lari} GEL, {self.tetri} tetri"

#     def __add__(self, other):
#         dollari = self.dollari + other.dollari
#         lari = self.lari + other.lari
#         tetri = self.tetri + other.tetri
#         return Bank(dollari,lari,tetri)

# giorgi = Bank(100, 50, 20)
# print(giorgi)

# lasha = Bank(250, 100, 60)
# print(lasha)

# total = giorgi + lasha
# print(total)
# import random

# class Student:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

#     def __str__(self):
#         return f"{self.name} swavlobs {self.subject}"

#     def grade(self, subject):
#         return f"{self.subject} grade {random.choice([1,2,3,4,5])}"

# name = "Giorgi"
# name.split()

# name = Student("Giorgi", "Math")
# print(name.grade("Math"))

# print(name.name)
# print(dir(name))

from tabulate import tabulate

class Dog:
    def __init__(self,gender,breed,age,color,weight):
        if gender not in ["M", "F"]:
            raise ValueError
        self.gender = gender
        self.breed = breed
        self.age = age
        self.color = color
        self.weight = weight

    def __str__(self):
        data_list = [[self.gender],[self.breed],[str(self.age)],[self.color],[str(self.weight)]]
        return tabulate(data_list, tablefmt="heavy_outline")

    def bark(self,name):
        return f"{name}, age: {self.age}, says WOOF!"

    def run(self):
        return f"{self.breed} is running!"
#getter
    @property
    def gender(self):
        return self._gender

#setter
    @gender.setter
    def gender(self,gender):
        if gender not in ["M", "F"]:
            raise ValueError
        self._gender = gender



    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        if name not in ["Giorgi", "Lasha", "Oto"]:
            raise ValueError("Invalid Name")
        self._name = name



class Retriever(Dog):
    def __init__(self,gender,breed,age,color,weight,type):
        super().__init__(gender,breed,age,weight,color)
        self.type = type

    def __str__(self):
        return f"{self.gender,self.breed,self.age,self.color,self.type}"

dog1 = Dog("F", "Pitbull", 5, "White", 20)
dog1.__gender = "fipasjfiposf"

# dog2 = Dog("M", "Pitbull", 2, "Black", 15)

dog2 = Retriever("M", "Retriever", 1, "Black", 20, "Golden")

print(dog2)



