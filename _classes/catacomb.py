from _classes.player import Player
from _classes.room import Room


class Catacomb:
    def __init__(self, player: Player):
        self.player: Player = player
        self._current_room: Room = None
        self.num_monsters: int = 0
        self.rooms: dict = {}
        self.x: int = 0
        self.y: int = 0

    def set_rooms(self, rooms: dict) -> None:
        self.rooms = rooms

    def set_current_room(self, room: Room) -> None:
        self._current_room = room

    def get_current_room(self) -> Room:
        return self._current_room
