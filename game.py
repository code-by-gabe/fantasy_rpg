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
    print("")


def play_game():
    welcome()
    input("Press ENTER to continue")
    explore_catacombs()


def explore_catacombs():
    while True:
        player_input = input("-> ").lower()

        if player_input == "help":
            print("TODO: add help function")
        elif player_input == "quit":
            print(
                "Overcome with terror, you flee the catacombs, and are forever branded a coward."
            )
            # TODO: Print out final score
            play_again()
        else:
            print("I don't understand you... type 'help' for help.")
            continue


def play_again():
    descision = input("Play again? (yes/no) -> ").lower()
    if descision == "yes":
        play_game()
    else:
        print("Until next time adventurer.")
        exit(0)
