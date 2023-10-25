# food = input("What food do you like? (q - quit): ")

# while not food == "q":
#     print(f"Your food: {food}")
#     food = input("What food do you like? (q - quit): ")

# print(food)

# capitals = {
#     "Georgia": "Tbilisi",
#     "Germany": "Berlin",
#     "USA": "Washington D.C",
#     "France": "Paris"
# }


# capitals.get("Georgia")
# capitals.update({"Georgia":"Batumi"})
# capitals.pop("France")

# keys = capitals.keys()

# for key, value in capitals.items():
#     print(f"{key} ---- {value}")


#1. დაგენერირდეს ამ სიტყვის შესაბამისი ქვედა ტირეები "_"

def main():
    word = "apple"
    print("Welcome to HANGMAN!")
    listed_word, listed_spaces = space_drawer(word)
    print(" ".join(listed_spaces))
    play_game(listed_word, listed_spaces)

def space_drawer(word):
    spaces = "_" * len(word)
    spaces = spaces.strip()
    listed_word = list(word)
    listed_spaces = list(spaces)
    return listed_word, listed_spaces

def play_game(listed_word, listed_spaces):
    # listed_word = ["a", "p","p","l","e"]
    # listed_spaces = ["_","_","_","_","_"]
    tries = 6
    letters = []
    while True:
        ask = input("Guess your letter: ").lower()

        if ask in letters:
            print("Already guessed!")
        elif ask in listed_word:
            for element in range(len(listed_word)):
                if listed_word[element] == ask:
                    listed_spaces[element] = ask
            print(" ".join(listed_spaces))
        else:
            letters.append(ask)
            tries -=1

        if tries == 0:
            print("Out of tries")
            break
        if "_" not in listed_spaces:
            print("You WIN!")
            break
main()
