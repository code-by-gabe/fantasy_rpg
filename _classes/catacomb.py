from _classes.player import Player
from _classes.room import Room


class Catacomb:
    def __init__(self, player: Player):
        self.player: Player = player
        self.room: Room = None
        self.num_monsters: int = 0
        self.rooms: dict = {}
        self.x: int = 0
        self.y: int = 0

    def set_rooms(self, rooms: dict) -> None:
        self.rooms = rooms
