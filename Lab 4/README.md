# Scenario 13 — Minesweeper

A modular terminal-based Minesweeper game featuring hidden mines, safe-cell reveals, flood-fill expansion, and flags.

## Objective

Inspect the supplied starter code, understand how the modules interact, reproduce the original defect, and extend the game through four tasks. This assignment tests debugging, reasoning about state, and careful review of LLM-generated code.

## Provided Files

* `main.py` — Entry point.
* `game.py` — Command handling and game flow.
* `board.py` — Board state, neighbours, mines, revealing, and flags.
* `requirements.txt` — Dependency declaration.

## Setup

Use Python 3.9 or newer.

Run the game using:

```bash
python3 main.py
```

No additional package installation is required.

## Before Changing the Code

1. Run the untouched starter code.
2. Read all three Python files.
3. Play several turns and observe the behaviour.
4. Trace a reveal command from the command line through the board logic.
5. Reproduce the Task 1 defect before attempting to fix it.

## Tasks and Implemented Features

### Task 1 — Boundary-Safe Board Traversal

**Objective:** Ensure every coordinate visited by reveal and mine-counting logic is a valid board coordinate.

**Implementation:**

* Corrected neighbour traversal to prevent out-of-bounds coordinates.
* Ensured adjacent-mine counting uses valid neighbouring cells.
* Improved flood-fill behaviour for corners, edges, and interior cells.
* Prevented flood-fill from revealing flagged cells.

**Done when:** Valid reveals stay within the board, and zero-adjacent regions expand correctly from edges and corners.

### Task 2 — Complete Win and Flag Behaviour

**Objective:** Ensure flags and the win condition behave correctly.

**Implementation:**

* Preserved the existing flag command.
* Supported placing and removing flags.
* Prevented flagged cells from being revealed.
* Checked for a win when every non-mine cell has been revealed.
* Prevented invalid actions from corrupting board state.

**Done when:** Flags can be toggled, invalid actions do not corrupt state, and revealing all safe cells ends the game correctly.

### Task 3 — Difficulty Modes

**Objective:** Add Easy, Medium, and Hard modes without requiring additional data files.

**Implementation:**

* Added a difficulty-selection menu.
* Configured different board dimensions and mine counts for each mode.
* Kept board state in memory.
* Preserved reveal and flag commands across difficulty levels.

**Done when:** Every mode produces a valid board, and the existing commands continue to work.

### Task 4 — Action-Level Feedback

**Objective:** Provide concise feedback for each player reveal action.

**Implementation:**

* Added feedback for safe reveals and adjacent-mine counts.
* Added feedback when a zero-adjacent region expands.
* Kept player-facing feedback outside the internal flood-fill loop.
* Added messages for invalid commands, invalid coordinates, and attempts to reveal flagged or already-revealed cells.

**Done when:** Feedback is tied to actual player commands rather than individual flood-fill iterations.

## Commands

| Command     | Description            |
| ----------- | ---------------------- |
| `r row col` | Reveal a cell          |
| `f row col` | Place or remove a flag |
| `q`         | Quit the game          |

Coordinates start at `1`. Select a difficulty when prompted at the beginning of the game.

## Required Testing

Use the following checklist to verify the implementation.

* [ ] Corner cells.
* [ ] Edge cells.
* [ ] Centre cells.
* [ ] Zero-adjacent regions and flood-fill expansion.
* [ ] Mine hits.
* [ ] Repeated reveals.
* [ ] Flag placement and removal.
* [ ] Attempts to reveal flagged cells.
* [ ] Invalid coordinates and invalid commands.
* [ ] Easy, Medium, and Hard difficulty modes.
* [ ] Winning by revealing every non-mine cell.
* [ ] Feedback appears once per player reveal command.

Record the results of your tests and investigate any unexpected behaviour before submission.

## LLM Usage

An LLM may be used as a coding assistant, while the student remains responsible for understanding and testing the result.

* Inspect the existing code before requesting changes.
* Ask for explanations when a proposed change is unclear.
* Test generated code against the stated behaviour and edge cases.
* Keep the complete LLM chat history for submission.
* Do not replace the project with an unrelated implementation.
* Keep all game state in memory. Do not add CSV, JSON, SQLite, or other persistence.

## Submission Checklist

* [ ] Task 1 completed; the original defect was reproduced and fixed.
* [ ] Tasks 2–4 completed and tested.
* [ ] Boundary and invalid-input cases tested.
* [ ] No unnecessary external dependencies added.
* [ ] No persistent storage added.
* [ ] Code remains understandable and modular.
* [ ] Complete LLM chat-history link included.
* [ ] Before and after gameplay recordings prepared.

## Submission Deliverables

Submit only these three items:

1. **Before video:** A 10-second gameplay recording showing the original bug or broken behaviour before changes.
2. **After video:** A 10-second gameplay recording showing the bug fixed and the new features working.
3. **Chat/LLM link:** A link to the conversation page containing the complete chat history.

## Folder Structure

```text
scenario-01-minesweeper/
├── README.md
├── requirements.txt
├── main.py
├── game.py
└── board.py
```

## LLM Conversation Link

Add the shareable link to the complete ChatGPT conversation here:

(https://chatgpt.com/share/6ac73187-358c-83e8-a586-4b31e6965b60)
