import unittest
from src.gameImplementation import Connect4

class TestConnect4(unittest.TestCase):
    """
    Unit tests for the Connect4 implementation.

    Each test focuses on a specific aspect of game behavior, such as:
    - initial state correctness
    - move application
    - winning condition detection
    - draw-state detection
    - blocked-column behavior
    """

    def setUp(self):
        """
        Clear the global WIN_CACHE before each test.

        The Connect4 implementation uses a class-level cache to memoize win
        evaluations. Clearing ensures tests remain isolated and deterministic.
        """
        Connect4.WIN_CACHE.clear()

    def test_initial_state(self):
        """
        Test that a newly started game has:
        - player X to move
        - an empty 6×7 board
        - non-terminal game state
        """
        game = Connect4.start()
        self.assertEqual(game.to_move(), "X")
        for row in game.board:
            self.assertTrue(all(cell is None for cell in row))
        self.assertFalse(game.is_terminal())

    def test_rival_function(self):
        """
        Test that `rival(player)` correctly returns the opposing player.

        Ensures no incorrect behavior like returning the same player or
        a wrong symbol.
        """
        game = Connect4.start()
        self.assertEqual(game.rival("X"), "O")
        self.assertEqual(game.rival("O"), "X")

    def test_available_row(self):
        """
        Test `_available_row()` indirectly through `action_results()`.

        A fresh board should allow 7 children (one for each column), and
        each resulting state should switch the player to O.
        """
        game = Connect4.start()
        next_states = game.action_results()
        self.assertEqual(len(next_states), Connect4.COLS)
        for state in next_states:
            self.assertEqual(state.to_move(), "O")

    def test_winner_horizontal(self):
        """
        Test detection of a horizontal winning line.

        The bottom row contains four consecutive X's. The last move is
        positioned so that `_winner()` can detect the line properly.
        """
        board = [[None]*7 for _ in range(6)]
        board[5][:4] = ["X", "X", "X", "X"]
        game = Connect4(board, player="O", last_move=(5, 3))
        self.assertEqual(game._winner(), "X")
        self.assertTrue(game.is_terminal())
        self.assertEqual(game.heuristic_utility("X"), 10000)
        self.assertEqual(game.heuristic_utility("O"), -10000)

    def test_winner_vertical(self):
        """
        Test detection of a vertical winning line.

        Column 0 contains four consecutive O's from rows 2–5.
        """
        board = [[None]*7 for _ in range(6)]
        for i in range(4):
            board[2+i][0] = "O"
        game = Connect4(board, player="X", last_move=(5, 0))
        self.assertEqual(game._winner(), "O")
        self.assertTrue(game.is_terminal())

    def test_winner_diagonal(self):
        """
        Test detection of a downward-right diagonal winning line.

        Coordinates:
            (2,0), (3,1), (4,2), (5,3) all contain X.
        """
        board = [[None]*7 for _ in range(6)]
        board[2][0] = "X"
        board[3][1] = "X"
        board[4][2] = "X"
        board[5][3] = "X"
        game = Connect4(board, player="O", last_move=(5, 3))
        self.assertEqual(game._winner(), "X")
        self.assertTrue(game.is_terminal())

    def test_full_board_draw(self):
        """
        Test a completely full board with no four-in-a-row.

        Ensures:
        - game is terminal
        - no winner is detected
        - heuristic utility is 0 for both players
        """
        board = [
            ["X", "X", "O", "O", "X", "X", "O"],
            ["O", "O", "X", "X", "O", "O", "X"],
            ["X", "X", "O", "O", "X", "X", "O"],
            ["O", "O", "X", "X", "O", "O", "X"],
            ["X", "X", "O", "O", "X", "X", "O"],
            ["O", "O", "X", "X", "O", "O", "X"]
        ]
        game = Connect4(board, player="X", last_move=None)
        self.assertTrue(game.is_terminal())
        self.assertIsNone(game._winner())
        self.assertEqual(game.heuristic_utility("X"), 0)

    def test_action_results_blocked_column(self):
        """
        Test that fully filled columns are not included in `action_results()`.

        Column 0 is filled bottom-to-top; the game should provide only 6 possible moves.
        """
        board = [[None for _ in range(7)] for _ in range(6)]
        vals = ["X", "O", "X", "O", "X", "O"]
        for r in range(6):
            board[5 - r][0] = vals[r]

        game = Connect4(board, player="O", last_move=None)

        moves = game.action_results()

        self.assertEqual(len(moves), Connect4.COLS - 1)


if __name__ == "__main__":
    unittest.main()
