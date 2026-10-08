import random

# Default difficulty
DEFAULT_ROWS = 6
DEFAULT_COLS = 6
DEFAULT_MINES = 6

# Difficulty configurations: (rows, columns, mines)
DIFFICULTIES = {
    "easy": (6, 6, 6),
    "medium": (9, 9, 15),
    "hard": (12, 12, 30),
}


class Board:
    def __init__(self, rows=DEFAULT_ROWS, cols=DEFAULT_COLS, mines=DEFAULT_MINES):
        if rows < 1 or cols < 1:
            raise ValueError("Rows and columns must be positive.")

        if not 0 <= mines < rows * cols:
            raise ValueError("Mine count must be non-negative and less than the board size.")

        self.rows = rows
        self.cols = cols
        self.mine_total = mines
        self.mines = self._build_mines()
        self.revealed = set()
        self.flags = set()

    @classmethod
    def from_difficulty(cls, difficulty):
        """Create a board using a named difficulty."""
        difficulty = difficulty.lower().strip()

        if difficulty not in DIFFICULTIES:
            raise ValueError("Choose easy, medium, or hard.")

        rows, cols, mines = DIFFICULTIES[difficulty]
        return cls(rows, cols, mines)

    def _build_mines(self):
        cells = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
        ]
        return set(random.sample(cells, self.mine_total))

    def in_bounds(self, r, c):
        """Return True if a coordinate is inside the board."""
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors(self, r, c):
        """Yield only valid neighboring coordinates."""
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r + dr, c + dc

                # FIX: indexes must be strictly less than dimensions.
                if self.in_bounds(nr, nc):
                    yield nr, nc

    def adjacent_mines(self, r, c):
        """Count mines surrounding a cell."""
        return sum(
            neighbor in self.mines
            for neighbor in self.neighbors(r, c)
        )

    def reveal(self, start):
        """
        Reveal a cell and expand through zero-adjacent safe cells.
        Returns True if a mine was hit, otherwise False.
        """
        if not self.in_bounds(*start):
            return False

        # A flagged or already-revealed cell cannot be revealed.
        if start in self.flags or start in self.revealed:
            return False

        stack = [start]
        hit_mine = False

        while stack:
            pos = stack.pop()

            if pos in self.revealed or pos in self.flags:
                continue

            r, c = pos

            if not self.in_bounds(r, c):
                continue

            self.revealed.add(pos)

            if pos in self.mines:
                hit_mine = True
                continue

            # Expand the zero-adjacent region.
            if self.adjacent_mines(r, c) == 0:
                for neighbor in self.neighbors(r, c):
                    if (
                        neighbor not in self.revealed
                        and neighbor not in self.flags
                        and neighbor not in self.mines
                    ):
                        stack.append(neighbor)

        return hit_mine

    def toggle_flag(self, pos):
        """Toggle a flag; revealed or invalid cells cannot be flagged."""
        if not self.in_bounds(*pos) or pos in self.revealed:
            return False

        if pos in self.flags:
            self.flags.remove(pos)
        else:
            self.flags.add(pos)

        return True

    def won(self):
        """Win only when every safe cell has been revealed."""
        safe_cells = {
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
            if (r, c) not in self.mines
        }

        return safe_cells.issubset(self.revealed)
