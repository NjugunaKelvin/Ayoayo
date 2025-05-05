from player import Player

class Ayoayo:
    def __init__(self):
        # Board set up:
        self._board = [[4] * 6, 0, [4] * 6, 0]  # [P1 pits, P1 store, P2 pits, P2 store]
        self._players = []
        self._game_ended = False
        self._current_player = 1  # Player 1 starts

    def create_player(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a valid, non-empty string.")
        if len(self._players) >= 2:
            raise ValueError("Only two players can play this game.")

        player_number = len(self._players) + 1
        new_player = Player(name.strip(), player_number)
        self._players.append(new_player)
        return new_player

    def print_board(self):
        print("\n" + "=" * 40)
        print("Current Board".center(40))
        print("=" * 40)

        # Bottom side (Player 1)
        print(f"\n{'Player 1 (' + self._players[0].name + ')':^40}")
        print(f"{'Store: ' + str(self._board[1]):^40}")
        print("Pits: ", end="")
        for i, seeds in enumerate(self._board[0], 1):
            print(f"{i}:{seeds}", end="  ")

        # Top side (Player 2)
        print(f"\n\n{'Player 2 (' + self._players[1].name + ')':^40}")
        print(f"{'Store: ' + str(self._board[3]):^40}")
        print("Pits: ", end="")
        for i, seeds in enumerate(self._board[2], 1):
            print(f"{i}:{seeds}", end="  ")
        print("\n" + "=" * 40 + "\n")

    def return_winner(self):
        if not self._game_ended:
            return None

        p1_score = self._board[1]
        p2_score = self._board[3]

        if p1_score == p2_score:
            return "tie"
        return self._players[0] if p1_score > p2_score else self._players[1]

    def get_current_player(self):
        return self._current_player

    def play_game(self, player_idx, pit_idx):
        if self._game_ended:
            return "Game over. No more moves allowed."
        if player_idx not in [1, 2]:
            return "Player index must be 1 or 2."
        if pit_idx < 1 or pit_idx > 6:
            return "Pit index must be between 1 and 6."

        pits = self._board[0] if player_idx == 1 else self._board[2]
        pit_idx -= 1  # Convert to 0-based index

        if pits[pit_idx] == 0:
            return "This pit is empty. Pick another one."

        seeds = pits[pit_idx]
        pits[pit_idx] = 0
        pos = pit_idx
        extra_turn = False
        store = 1 if player_idx == 1 else 3

        # Distribute seeds
        while seeds > 0:
            pos += 1

            if pos >= len(pits):
                self._board[store] += 1
                seeds -= 1
                if seeds == 0:
                    extra_turn = True
                pos = -1  # Loop back
                continue

            if player_idx == 1:
                if pos < len(pits):
                    pits[pos] += 1
                else:
                    self._board[2][pos - len(pits)] += 1
            else:
                if pos < len(pits):
                    pits[pos] += 1
                else:
                    self._board[0][pos - len(pits)] += 1
            seeds -= 1

        # Check capture
        if not extra_turn and pos != -1 and pits[pos] == 1:
            opp_pos = 5 - pos
            opp_pits = self._board[2] if player_idx == 1 else self._board[0]
            if opp_pits[opp_pos] > 0:
                self._board[store] += opp_pits[opp_pos] + 1
                opp_pits[opp_pos] = 0
                pits[pos] = 0

        self._check_game_end()

        if not extra_turn:
            self._current_player = 2 if self._current_player == 1 else 1
        else:
            print(f"\n{self._players[player_idx - 1].name} gets an extra turn!")

        return None

    def _check_game_end(self):
        p1_empty = all(s == 0 for s in self._board[0])
        p2_empty = all(s == 0 for s in self._board[2])

        if p1_empty or p2_empty:
            self._game_ended = True
            if p1_empty:
                self._board[3] += sum(self._board[2])
                self._board[2] = [0] * 6
            else:
                self._board[1] += sum(self._board[0])
                self._board[0] = [0] * 6
