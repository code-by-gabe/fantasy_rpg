from colorama import Fore, init
from blessed import Terminal
from _classes.player import Player
from _classes.room import Room
from _classes.catacomb import Catacomb


def play_game() -> None:
    terminal = Terminal()
    print(terminal.clear())

    # init() makes sure colorama works on various platforms.
    init()

    adventurer = Player()
    current_catacomb = Catacomb(adventurer)

    room = Room()

    current_catacomb.set_current_room(room)

    welcome()

    input(f"{Fore.WHITE}Press ENTER to continue{Fore.RESET}")
    explore_catacombs(current_catacomb)


def welcome() -> None:
    print(f"{Fore.RED}\t\t\t\t\t\tCATACOMBS OF THE OLD ONES{Fore.RESET}")
    print(
        f"""{Fore.WHITE}
    The village of Innsburg has been terrorised by strange, other-worldly creatures for months now. Unable to endure 
    any longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the catacombs where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a pistol, your journal from the Miskatonic university, and a few flares, 
    you descend into the catacombs, where only madness awaits...{Fore.RESET}

    """
    )


def explore_catacombs(current_catacomb: Catacomb) -> None:
    while True:
        current_catacomb.get_current_room().print_description()

        player_input = input(f"{Fore.MAGENTA}-> {Fore.RESET}").lower()

        if player_input == "journal":
            show_journal()
        elif player_input == "quit":
            print(
                f"{Fore.WHITE}Overcome with terror, you flee the catacombs, and are forever branded a coward.{Fore.RESET}"
            )
            # TODO: Print out final score
            play_again()
        else:
            print(
                f"{Fore.WHITE}Have you been stricken by madness!? If you need help, type 'journal'.{Fore.RESET}"
            )
            continue


def show_journal() -> None:
    print(
        f"""{Fore.WHITE}Enter a command: 
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
    - quit - end the game{Fore.RESET}"""
    )


def play_again() -> None:
    yes_no = get_yes_no(f"{Fore.WHITE}Do you want to play again?{Fore.RESET}")
    if yes_no == "yes":
        play_game()
    else:
        print(f"{Fore.WHITE}Until next time adventurer.{Fore.RESET}")
        exit(0)


def get_yes_no(question: str) -> str:
    while True:
        answer = (
            input(f"{question}{Fore.WHITE} (yes/no) {Fore.MAGENTA}-> {Fore.RESET}")
            .lower()
            .strip()
        )
        if answer not in ["yes", "no", "y", "n"]:
            print(f"{Fore.WHITE}Please enter yes or no.{Fore.RESET}")
        else:
            if answer == "y":
                answer = "yes"
            elif answer == "n":
                answer = "no"
            return answer
