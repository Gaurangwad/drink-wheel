import random

# Define the drink options and their probabilities
drinks = ["absolut", "bacardi", "old monk", "beer today", "jonnie walker"]
probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

# Define a function to spin the wheel and return the drink
def spin_wheel():
    # Use the probabilit
    # ies to determine which drink was won
    drink_index = random.choices(range(len(drinks)), weights=probabilities)[0]
    return drinks[drink_index]

# Define a function to play the game
def play_game():
    # Ask the player to spin the wheel
    input("Press Enter to spin the wheel...")

    # Spin the wheel and get the drink
    drink = spin_wheel()

    # Tell the player what drink they should drink
    print("Okay then! You should drink:", drink)

# Play the game
play_game()

