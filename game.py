import random

from colorama import Fore, init
from blessed import Terminal

from _classes.player import Player
from _classes.room import Room
from _classes.catacomb import Catacomb

from _text_files.armory import equipment
from _text_files.bestiary import monsters


def play_game() -> None:
    terminal = Terminal()
    print(terminal.clear())

    # init() makes sure colorama works on various platforms.
    init()

    adventurer = Player()
    current_catacomb = Catacomb(adventurer)
    welcome()

    input(f"{Fore.WHITE}Press ENTER to continue{Fore.RESET}")
    print("")

    explore_catacombs(current_catacomb)


def welcome() -> None:
    print(f"{Fore.RED}\t\t\t\t\t\tCATACOMBS OF THE OLD ONES{Fore.RESET}")
    print(
        f"""{Fore.WHITE}
    The village of Innsburg has been terrorised by strange, other-worldly creatures for months now. Unable to endure 
    any longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the catacombs where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword, your journal, and a bundle of torches, 
    you descend into the catacombs, where only death awaits.{Fore.RESET}

    """
    )


def generate_room() -> Room:
    items = []
    monster = {}

    # 25% chance of an item.
    if random.randint(1, 100) < 26:
        item = random.choice(list(equipment.values()))
        items.append(item)

    # 25% of a monster
    if random.randint(1, 100) < 26:
        monster = random.choice(monsters)

    return Room(items, monster)


def explore_catacombs(current_catacomb: Catacomb) -> None:
    while True:
        room = generate_room()

        current_catacomb.set_current_room(room)
        current_catacomb.get_current_room().print_description()

        for item in current_catacomb.get_current_room().items:
            print(f"{Fore.MAGENTA}You see a {item['name']}{Fore.RESET}.")

        if current_catacomb.get_current_room().monster:
            print(
                f"{Fore.RED}There is a {current_catacomb.get_current_room().monster['name']}!"
            )

        player_input = input(f"{Fore.MAGENTA}-> {Fore.RESET}").lower().strip()

        if player_input == "journal":
            show_journal()
        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.WHITE}You move deeper into the catacombs.")
            continue
        elif player_input == "quit":
            print(
                f"{Fore.WHITE}Overcome with terror, you flee the catacombs, and are forever branded a coward.{Fore.RESET}"
            )
            # TODO: Print out final score
            play_again()
        else:
            print(
                f"{Fore.WHITE}Are you ok adventurer? If you need help, type 'journal'.{Fore.RESET}"
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
