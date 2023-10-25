# სავარჯიშო 3 - მისალმებები
# შექმენით პროგრამა, რომელიც იკითხავს მომხამრებლის მისასალმებელ ინფუთს

# თუ მისალმება იწყება hello-თი, მაშინ დაბეჭდავს "You're friendly!"
# თუ მისალმებაში არის "python"-ი, მაშინ დაბეჭდავს "You're a Python enthusiast!"
# თუ მისალმება მთავრდება !-ით, მაშინ დაბეჭდავს "You're excited!"
# სხვა შემთხვევაში - "You're mysterious!"

def main():
    greeting = input("Please say your greeting: ").lower().strip()
    print(greeting_fun(greeting))


def greeting_fun(greeting):
    if greeting.startswith("hello"):
        return("You're friendly!")
    elif "python" in greeting:
        return("You're a Python enthusiast!")
    elif greeting.endswith("!"):
        return("You're excited!")
    else:
        return("You're mysterious!")


main()
