import random

from _text_files.descriptions import descriptions, smells, sounds


class Room:
    def __init__(self, items: list, monster: dict):
        self.description: str = descriptions[random.randint(0, len(descriptions) - 1)]
        self.smell: str = smells[random.randint(0, len(smells) - 1)]
        self.sound: str = sounds[random.randint(0, len(sounds) - 1)]
        self.items: list = items
        self.monster: dict = monster

    def print_description(self) -> None:
        print(self.description)
        print(self.smell)
        print(self.sound)
