from game import Ayoayo

def main():
    print("""
    === Welcome to Ayoayo! ===
    
    A classic African seed-sowing game.
    Goal: Capture more seeds than your opponent.
    """)

    game = Ayoayo()

    # Setup
    p1_name = input("Player 1, enter your name: ").strip()
    p2_name = input("Player 2, enter your name: ").strip()

    game.create_player(p1_name)
    game.create_player(p2_name)

    while True:
        game.print_board()
        current_player = game.get_current_player()
        player_name = game._players[current_player - 1].name

        print(f"\n{player_name}'s turn (Player {current_player})")
        print("Pick a pit (1-6) or type 'q' to quit:")

        while True:
            choice = input("> ").strip().lower()
            if choice == 'q':
                print("\nGame stopped. See you next time!")
                return

            try:
                pit_num = int(choice)
                feedback = game.play_game(current_player, pit_num)
                if feedback:
                    print(f"⚠️  {feedback}")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number from 1 to 6, or 'q' to quit.")

        winner = game.return_winner()
        if winner == "tie":
            print("\nIt's a draw! Well played both.")
            game.print_board()
            break
        elif winner:
            print(f"\n🎉 {winner.name} wins the game! Congratulations!")
            game.print_board()
            break

if __name__ == "__main__":
    main()
