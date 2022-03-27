class Player:
    def __init__(self):
        self.hp: int = 100
        self.treasure: int = 0
        self.monsters_killed: int = 0
        self.xp: int = 0
        self.turns_played: int = 0
        self.inventory: list = []
