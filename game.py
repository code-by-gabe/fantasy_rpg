def welcome():
    print("")
    print(
        "                                                   CATACOMBS OF THE OLD ONES"
    )
    print(
        """
    The village of Innsburg has been terrorised by strange, other-worldly creatures for months now. Unable to endure 
    any longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the catacombs where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the catacombs, 
    where only madness awaits...
    """
    )


def play_game():
    welcome()
    input("Press ENTER to continue")
    explore_catacombs()


def explore_catacombs():
    while True:
        player_input = input("-> ").lower()

        if player_input == "help":
            show_help()
        elif player_input == "quit":
            print(
                "Overcome with terror, you flee the catacombs, and are forever branded a coward."
            )
            # TODO: Print out final score
            play_again()
        else:
            print("Have you been stricken by madness!? Do you need 'help'?")
            continue


def play_again():
    descision = input("Play again? (yes/no) -> ").lower()
    if descision == "yes":
        play_game()
    else:
        print("Until next time adventurer.")
        exit(0)


def show_help():
    print(
        """Enter a command: 
    - n/s/e/w: move in a direction
    - map - show a map of the labyrinth
    - look - look around and describe your environment
    - equip <item> - use an item from your inventory
    - unequip <item> - stop using an item from your inventory
    - fight - attack a foe
    - examine <object> - examine an object more closely
    - get <item> - pick up an item
    - drop <item> - drop an item
    - rest - restore some health by resting
    - inventory - show your inventory
    - status - show current player status
    - quit - end the game"""
    )
