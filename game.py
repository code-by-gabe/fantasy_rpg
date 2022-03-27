from os import curdir
import random

from colorama import Fore, init
from blessings import Terminal

from _classes.player import Player
from _classes.room import Room
from _classes.catacomb import Catacomb

from _text_files.armory import equipment
from _text_files.bestiary import monsters

from _utils import sequence_utils


def play_game() -> None:
    terminal = Terminal()
    print(terminal.clear())

    # init() makes sure colorama works on various platforms.
    init()

    adventurer = Player()
    current_catacomb = Catacomb(adventurer)
    current_catacomb.room = generate_room()
    welcome()

    input(f"{Fore.MAGENTA}Press ENTER to continue{Fore.RESET}")
    print("")

    current_catacomb.room.print_description()

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
        for item in current_catacomb.room.items:
            print(f"{Fore.YELLOW}You see a {item['name']}{Fore.RESET}.")

        if current_catacomb.room.monster:
            print(f"{Fore.RED}There is a {current_catacomb.room.monster['name']}!")

        player_input = input(f"{Fore.MAGENTA}-> {Fore.RESET}").lower().strip()

        if player_input == "journal":
            show_journal()
        elif player_input.startswith("get"):
            if not current_catacomb.room.items:
                print("There is nothing to pick up.")
                continue
            else:
                get_item(current_catacomb, player_input)
                continue
        elif player_input in ["inventory", "inv"]:
            show_inventory(current_catacomb)
            continue
        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.WHITE}You move deeper into the catacombs.")
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

        current_catacomb.room = generate_room()
        current_catacomb.room.print_description()


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


def show_inventory(current_catacomb: Catacomb):
    print(f"{Fore.WHITE}Your inventory:{Fore.RESET}")
    for item in current_catacomb.player.inventory:
        print(f"\t - {item.capitalize()}")


def get_item(current_catacomb: Catacomb, player_input: str):
    if len(current_catacomb.room.items) > 0 and player_input[4:] == "":
        player_input = f"{player_input} {current_catacomb.room.items[0]['name']}"

    if player_input[4:] not in current_catacomb.player.inventory:
        item_index = sequence_utils.find_in_list(
            player_input[4:], "name", current_catacomb.room.items
        )

        if item_index > -1:
            current_item = current_catacomb.room.items[item_index]
            current_catacomb.player.inventory.append(current_item["name"])
            current_catacomb.room.items.pop(item_index)
            print(f"{Fore.MAGENTA}You pick up the {current_item['name']}.{Fore.RESET}")
        else:
            print(f"{Fore.RED}There is no {player_input[4:]} here!{Fore.RESET}")
    else:
        print(
            f"{Fore.YELLOW}You already have a {player_input[4:]}, and decide to leave this one.{Fore.RESETs}"
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
