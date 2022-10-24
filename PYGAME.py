import random
print("+----------------------+")
print("|-----WHACK A MOLE-----|")
print("+----------------------+")
class User:
    def __init__(self, username):
        self.username = username


user = User(input("Please enter a username: "))
print("Welcome,", user.username)

def generate_pointer():
    pointer = random.randint(1,10)
    return pointer

class Game(User):
    @classmethod
    def user_guess(cls):
        get_pointer = generate_pointer()
        score = 0
        while score < 1:
            user_input = int(input("Please enter a number between 1 and 9: "))
            if user_input == get_pointer:
                print("HIT!")
                score =+ 1
            else:
                print("MISS!")
        print(user.username,", your score is:",score)
Game.user_guess()