class Player:
    def __init__(self, name, player_num):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Player name must be a non-empty string")
        if player_num not in [1, 2]:
            raise ValueError("Player number must be 1 or 2")

        self.name = name.strip()
        self.player_num = player_num  # Player 1 or Player 2

    def __repr__(self):
        return f"<Player {self.player_num}: {self.name}>"
