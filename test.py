###### WHACK A MOLE GAME #########

print("+----------------------+")
print("|------MAIN MENU-------|")
print("|----------------------|")
print("|--1. PLAY GAME--------|")
print("|--0. SETTINGS---------|")
print("|--0. EXIT GAME--------|")
print("+----------------------+")
print("\n")
try:
    user_input = int(input("Please enter a number: "))
    if user_input == 1:
        from Game import Game
    elif user_input == 2:
        from Settings import Settings
    elif user_input < 2:
        print("Number is out of range!")
    elif user_input == 0:
        quit()
except ValueError:
    print("Invalid Input! Must be a number.")
except Exception:
    print("Could not gather a file.")
