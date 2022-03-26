import random

from _text_files.descriptions import descriptions, smells, sounds


class Room:
    def __init__(self):
        self.description: str = descriptions[random.randint(0, len(descriptions) - 1)]
        self.smell: str = smells[random.randint(0, len(smells) - 1)]
        self.sound: str = sounds[random.randint(0, len(sounds) - 1)]

    def print_description(self) -> None:
        print(self.description)
        print(self.smell)
        print(self.sound)
