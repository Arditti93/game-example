import time
global name

def level_two(name):
    print("level two function")


def level_one(name):
    print(f"{name} you find yourselve with three doors")
    time.sleep(3)
    print("Which door do you choose?")
    time.sleep(3)
    print("left, middle or right")
    time.sleep(3)
    user_choice = input("Which do you choose? ")
    if user_choice == "Right" or user_choice == "r":
        print("Sorry you died, start again")
        start_game()
    elif user_choice == "Middle" or user_choice == "M":
        print("Sorry you died, start again")
        start_game()
    elif user_choice == "Left" or user_choice == "L":
        level_two(name)
    else:
        print("Sorry i didn't get that")
        level_one(name)
    
def start_game():
    name = input("Please enter your name: ")
    time.sleep(3)
    print(f"Hello {name} welcome to the game")
    time.sleep(3)
    is_ready = input("Are yo ready? [Yes/No] ")

    if is_ready == "Yes" or is_ready == "yes" or is_ready == "y":
        level_one(name)
    else:
        return
    

start_game()

 