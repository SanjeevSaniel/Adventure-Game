import time
import random

# List containing the villanious characters
villains = ["monster", "maleficent", "fire-dragon"]
random_choice = random.choice(villains)


# Function to display the appropriate message
def display(message):
    print(message)
    time.sleep(1)


# Display game start message context
def start():
    display("You find yourself standing in an open field, "
            "filled with grass and surrounded by oak trees.")
    display("There's a hearsay that a maleficent is somewhere around here, "
            "and has been terrifying the nearby village from past decades.")
    display("In front of you there is a abandoned 'Villa'.")
    display("Toward the right is a very old cave.")
    display("On your hand you hold your trustworthy "
            "(not so powerfull) dagger.\n")


# Choosing either to get into the 'Villa' or run away.
def choose():
    display("Enter 1 to knock on the door of the 'Villa'.")
    display("Enter 2 to peer into the cave.")
    display("What would you like to do?")
    display("(Please enter 1 or 2).")


# Functions for random stories
def story1(villains):
    display(f"You are about to knock but before then "
            f"the door opens and steps out a {villains[0]}.")
    display(f"Oh,no! This is the {villains[0]}'s house!")
    display("The monster attacks you!")


def story2(villains):
    display(f"You are about to knock but before then "
            f"the door opens and steps out a {villains[1]}.")
    display(f"Oh,no! This is the {villains[1]}'s house!")
    display("The maleficent attacks you!")


def story3(villains):
    display(f"You are about to knock but before then "
            f"the door opens and steps out a {villains[2]}.")
    display(f"Oh,no! This is the {villains[2]}'s house!")
    display("The fire-dragon attacks you!")


def defeat(random_choice):
    display(f"but your dagger is no match for the {random_choice}.")


def fight(villains):
    display("You do your best...")
    if "monster" in random_choice:
        defeat(random_choice)

    elif "maleficent" in random_choice:
        defeat(random_choice)

    elif "fire-dragon" in random_choice:
        defeat(random_choice)

    display("You have been defeated!\n")
    display("GAME OVER!\n")
    display("Would you like to play again? (yes/no) ")
    y_n = input()
    if y_n == "y" or y_n == "yes":
        display("Magnificent! Rebooting the game ...")
        play_again()

    elif y_n == "n" or y_n == "no":
        display("Thanks for playing! See ya next time.")
    return


def run():
    display("You run back into the field. "
            "Luckily, you don't seem to have been followed.")
    display("Let's follow once more\n")


def choice_one():
    display("You move towards the door of the 'Villa'.")
    if "monster" in random_choice:
        story1(villains)

    elif "maleficent" in random_choice:
        story2(villains)

    elif "fire-dragon" in random_choice:
        story3(villains)

    display("You feel a bit under-prepared for this, "
            "what with only having a tiny dagger.")
    display("Would you like to (1) fight or (2) run away?")
    option = input()
    if option == "1":
        fight(villains)
    elif option == "2":
        run()
        choose()
        choice()
    else:
        choice_one()


def choice_two():
    display("You peer cautiously towars the forest.")
    display("It turns out to be only a small bushes.")
    display("Your eye catches a glint of metal behind a rock.")
    display("You have found the magical Sword of Ogoroth!")
    display("You discard your silly old dagger and take the sword with you.")
    display("You walk back out to the field.\n")


def choice():
    choice_input = input()
    if choice_input == "1" or choice_input == "one":
        choice_one()

    elif choice_input == "2" or choice_input == "two":
        choice_two()
        choose()
        c = input()
        if c == "2":
            display("You peer cautiously toward the forest.")
            display("You've been here before, and gotten all the good stuff. "
                    "It's just a movement of some animal.")
            display("You walk back out to the field.\n")
            ran_away()

        else:
            choice_one()
            choice()

    else:
        display("(Please enter 1 or 2).")
        choose()
        choice()


def ran_away():
    choose()
    choice()


# Main Function
def play_again():
    start()
    ran_away()


# Main Function Call
if __name__ == "__main__":
    play_again()
