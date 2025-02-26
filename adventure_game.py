import random
import time

def start_game():
    """Starts the game with a welcome message and an introduction."""
    name = input("Welcome! Please type in your name: ")
    print(f"Hello, {name}! Welcome to the adventure game!")
    
    # Setting up the backstory
    print("""
    You are a treasure hunter searching for the legendary Golden Chalice, 
    hidden deep in the Forbidden Forest. Beware, many dangers lie ahead.
    """)
    
    play_game()

def play_game():
    """Checks if the player wants to play and initiates the game."""
    should_we_play = input("Do you want to play? (yes/no): ").lower()
    
    if should_we_play in ("yes", "y"):
        print("Great! Let's start your adventure!")
        choose_direction()
    else:
        print("Maybe next time! Goodbye.")
        exit()  # Ends the game if they don't want to play.

def choose_direction():
    """Presents the first choice: left or right."""
    print("You are at the edge of a dark forest. The path splits into two.")
    direction = input("Do you want to go left or right? (left/right): ").lower()

    if direction == "left":
        print("""
        You went left and encountered a group of wild wolves. 
        With no way to escape, you were overwhelmed. Game over.
        """)
    elif direction == "right":
        encounter_bridge()
    else:
        print("Invalid choice! You hesitate too long and are attacked by bandits. Game over.")

def encounter_bridge():
    """Presents the bridge scenario with an option to pick up an item."""
    print("You walk further and find a stick on the ground.")
    stick = input("Do you want to pick it up? (yes/no): ").lower()

    if stick in ("yes", "y"):
        print("You picked up the stick! This might come in handy later.")
        has_stick = True
    else:
        print("You ignored the stick. Hopefully, you won't regret it.")
        has_stick = False

    choice = input("You now see a bridge. Do you swim under it or cross it? (swim/cross): ").lower()

    if choice == "swim":
        print("""
        You decide to swim under the bridge, but a hungry alligator spots you.
        """)
        if has_stick:
            print("You used the stick to fend off the alligator and survive! You continue your journey.")
            find_treasure()
        else:
            print("Without a weapon, the alligator attacks you. Game over.")
    elif choice == "cross":
        print("You safely cross the bridge and continue on your way.")
        find_treasure()
    else:
        print("Invalid choice! While you hesitate, the bridge collapses. Game over.")

def find_treasure():
    """Final scenario: find the treasure or face a final challenge."""
    print("After crossing the bridge, you find a hidden cave with the Golden Chalice!")
    print("But a dragon guards the treasure.")
    
    print("You need to solve a riddle to distract the dragon.")
    time.sleep(2)

    riddle = """
    I speak without a mouth and hear without ears. 
    I have no body, but I come alive with the wind. What am I?
    """
    print(riddle)
    answer = input("Your answer: ").lower()

    if answer == "echo":
        print("""
        The dragon is impressed by your wit and allows you to take the treasure.
        Congratulations, you won the game!
        """)
    else:
        print("""
        The dragon is angered by your incorrect answer and breathes fire.
        You didn't survive. Game over.
        """)

def countdown_timer(seconds):
    """Optional: Add a countdown timer for critical choices."""
    print("You have limited time to decide!")
    for i in range(seconds, 0, -5):
        print(i)
        time.sleep(1)

# Starting the game
start_game()
