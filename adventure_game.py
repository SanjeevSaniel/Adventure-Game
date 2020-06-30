import time
import random

villains = ["pirate", "wicked fairie", "dragon"]
random_choice = random.choice(villains)


def print_sleep(message):
    print(message)
    time.sleep(2)


def intro():
    print_sleep("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def choose():
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    print_sleep("(Please enter 1 or 2).")


# Functions for random stories
def story1(villains):
    print_sleep(
        f"You are about to knock when the door opens and out steps a {villains[0]}.")
    print_sleep(f"Eep! This is the {villains[0]}'s house!")
    print_sleep("The pirate attacks you!")


def story2(villains):
    print_sleep(
        f"You are about to knock when the door opens and out steps a {villains[1]}.")
    print_sleep(f"Eep! This is the {villains[1]}'s house!")
    print_sleep("The wicked fairie attacks you!")


def story3(villains):
    print_sleep(
        f"You are about to knock when the door opens and out steps a {villains[2]}.")
    print_sleep(f"Eep! This is the {villains[2]}'s house!")
    print_sleep("The dragon attacks you!")


def defeat(random_choice):
    print_sleep(f"but your dagger is no match for the {random_choice}.")


def fight(villains):
    print_sleep("You do your best...")
    if "pirate" in random_choice:
        defeat(random_choice)

    elif "wicked fairie" in random_choice:
        defeat(random_choice)

    elif "dragon" in random_choice:
        defeat(random_choice)

    print_sleep("You have been defeated!")
    print_sleep("GAME OVER!\n")
    print_sleep("Would you like to play again? (y/n) ")
    y_n = input()
    if y_n == "y" or y_n == "yes":
        print_sleep("Excellent! Restarting the game ...")
        play_again()

    elif y_n == "n" or y_n == "no":
        print_sleep("Thanks for playing! See you next time.")


def run():
    print_sleep("You run back into the field. "
                "Luckily, you don't seem to have been followed.\n")


def choice_one():
    print_sleep("You approach the door of the house.")
    if "pirate" in random_choice:
        story1(villains)

    elif "wicked fairie" in random_choice:
        story2(villains)

    elif "dragon" in random_choice:
        story3(villains)

    print_sleep("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")
    print_sleep("Would you like to (1) fight or (2) run away?")
    option = input()
    if option == "1":
        fight(villains)
    elif option == "2":
        run()
        choose()
        choice()


def choice_two():
    print_sleep("You peer cautiously into the cave.")
    print_sleep("It turns out to be only a very small cave.")
    print_sleep("Your eye catches a glint of metal behind a rock.")
    print_sleep("You have found the magical Sword of Ogoroth!")
    print_sleep("You discard your silly old dagger and take the sword with you.")
    print_sleep("You walk back out to the field.\n")


def choice():
    choice = input()
    if choice == "1":
        choice_one()

    elif choice == "2":
        choice_two()
        choose()
        c = input()
        if c == "2":
            print_sleep("You peer cautiously into the cave.")
            print_sleep("You've been here before, and gotten all the good stuff. "
                        "It's just an empty cave now.")
            print_sleep("You walk back out to the field.\n")
            ran_away()

        else:
            choice_one()
            choice()

    else:
        print_sleep("(Please enter 1 or 2).")
        choice()


def ran_away():
    choose()
    choice()


# Main Function
def play_again():
    intro()
    ran_away()


# Main Function Call
play_again()
