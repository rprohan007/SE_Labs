from board import Board, DIFFICULTIES


class Minesweeper:
    def __init__(self):
        self.board = None
        self.difficulty = None

    def select_difficulty(self):
        """Ask the player to select a difficulty."""
        print("\nSelect difficulty:")
        print("1. Easy   (6 x 6, 6 mines)")
        print("2. Medium (9 x 9, 15 mines)")
        print("3. Hard   (12 x 12, 30 mines)")

        choices = {
            "1": "easy",
            "2": "medium",
            "3": "hard",
            "easy": "easy",
            "medium": "medium",
            "hard": "hard",
        }

        while True:
            choice = input("Difficulty (1/2/3): ").strip().lower()

            if choice in choices:
                self.difficulty = choices[choice]
                self.board = Board.from_difficulty(self.difficulty)
                print(f"\n{self.difficulty.title()} mode selected.")
                return

            print("Invalid choice. Enter 1, 2, or 3.")

    def display(self, reveal_mines=False):
        """Display the current board."""
        b = self.board

        print("\n    " + " ".join(f"{c + 1:2}" for c in range(b.cols)))

        for r in range(b.rows):
            cells = []

            for c in range(b.cols):
                pos = (r, c)

                if reveal_mines and pos in b.mines:
                    ch = "*"
                elif pos in b.flags:
                    ch = "F"
                elif pos not in b.revealed:
                    ch = "#"
                elif pos in b.mines:
                    ch = "*"
                else:
                    count = b.adjacent_mines(r, c)
                    ch = str(count) if count > 0 else " "

                cells.append(f"{ch:2}")

            print(f"{r + 1:2}  " + " ".join(cells))

        print(f"\nFlags: {len(b.flags)}/{b.mine_total}")

    def run(self):
        """Run the Minesweeper game."""
        print("=== Minesweeper ===")
        self.select_difficulty()

        print("\nCommands:")
        print("  r row col  - Reveal a cell")
        print("  f row col  - Toggle a flag")
        print("  q          - Quit")

        while True:
            self.display()
            raw = input("\n> ").strip().lower()

            if raw == "q":
                print("Game ended.")
                return

            parts = raw.split()

            if len(parts) != 3 or parts[0] not in {"r", "f"}:
                print("Invalid command. Use: r row col, f row col, or q.")
                continue

            try:
                row = int(parts[1])
                col = int(parts[2])
            except ValueError:
                print("Coordinates must be whole numbers.")
                continue

            r, c = row - 1, col - 1

            if not self.board.in_bounds(r, c):
                print(
                    f"Outside the board. Rows: 1-{self.board.rows}, "
                    f"columns: 1-{self.board.cols}."
                )
                continue

            pos = (r, c)

            if parts[0] == "f":
                if self.board.toggle_flag(pos):
                    if pos in self.board.flags:
                        print(f"Flag placed at ({row}, {col}).")
                    else:
                        print(f"Flag removed from ({row}, {col}).")
                else:
                    print("Cannot flag a revealed cell.")
                continue

            # Reveal action: feedback is printed once per command,
            # never inside the board's flood-fill loop.
            if pos in self.board.flags:
                print("That cell is flagged. Remove the flag before revealing it.")
                continue

            if pos in self.board.revealed:
                print("That cell is already revealed.")
                continue

            hit_mine = self.board.reveal(pos)

            if hit_mine:
                self.display(reveal_mines=True)
                print("\nBOOM! You hit a mine. Game over.")
                return

            if self.board.won():
                self.display()
                print("\nCongratulations! You cleared all safe cells.")
                return

            count = self.board.adjacent_mines(r, c)

            if count == 0:
                print("Safe reveal! The empty region has been expanded.")
            else:
                print(f"Safe reveal! {count} adjacent mine(s).")
