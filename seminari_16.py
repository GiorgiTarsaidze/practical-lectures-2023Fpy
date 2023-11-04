user_data = {
    "John": {"age": 25, "email": "john@example.com"},
    "Alice": {"age": 30, "email": "alice@example.com"},
    "Bob": {"age": 28, "email": "bob@example.com"},

}


def add_user(name, age, email):
    #       "Giorgi"
    if name not in user_data:
        user_data[name] = {"age" : age, "email" : email}
        return True

    return False

def delete_user(name):
    if name in user_data:
        user_data.pop(name)
        return True
    return False

def update_user(name, age=None, email=None):
    if name in user_data:
        if age:
            user_data[name]["age"] = age
        if email:
            user_data[name]["email"] = email
        return True
        # for element in user_data[name]:
        #     if element != None:
        #         user_data[name] = {}

    return False


def find_user(name):
    if name in user_data:
        return user_data[name]

    return False


# name = input("name: ")
# age = input("age: ")
# if age == "":
#     age = None
# email = input("email: ")

# update_user("Bob", 29)

print(find_user("Bob"))
print(user_data)

# delete_user("John")
# add_user("Giorgi", 28, "giorgi@example.com")




# unittest
# nose
# pytest

# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

# if __name__ == '__main__':
#     unittest.main()

# pytest:
