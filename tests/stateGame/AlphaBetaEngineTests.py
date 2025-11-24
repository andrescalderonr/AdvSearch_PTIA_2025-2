import unittest
from src.gameImplementation.Connect4 import Connect4
from src.stateGame.AlphaBetaEngine import AlphaBetaEngine

class TestAlphaBetaEngine(unittest.TestCase):

    def test_terminal_state_evaluation(self):
        """
        Verify that the engine recognizes a terminal (winning) board and returns
        the expected evaluation from the maximizing player's perspective.

        Setup
        - Create an empty 6x7 board.
        - Place four "X" tokens in the bottom row columns 0..3 to form an immediate win.
        - Instantiate the game/engine with player="O" and last_move pointing to the
          last placed token (5, 3).

        Expectation
        - Calling engine.max_value(...) should return the engine's terminal loss
          score for the current player (here asserted as -10000).
        """
        board = [[None]*7 for _ in range(6)]
        board[5][:4] = ["X", "X", "X", "X"]

        game = Connect4(board, player="O", last_move=(5, 3))
        engine = AlphaBetaEngine()

        result = engine.max_value(game, depth=3, alpha=-10 ** 9, beta=10 ** 9)
        
        self.assertEqual(result, -10000)

    def test_search_selects_best_move(self):
        """
        Ensure the search routine selects a winning move for the maximizing player.

        Setup
        - Start from the standard initial board via EngineConnect4.start().
        - Build a vertical threat for "X" in column 3 by placing three "X" tokens
          at rows 5, 4, 3 (so a move in column 3 completes a 4-in-a-row).
        - Instantiate the game/engine with player="X" and last_move=(3, 3).

        Expectation
        - engine.search(game, depth=2) returns a game state whose last_move column
          is 3 (the winning move).
        """
        game = Connect4.start()

        board = game.board
        board[5][3] = "X"
        board[4][3] = "X"
        board[3][3] = "X"

        game = Connect4(board, player="X", last_move=(3, 3))
        engine = AlphaBetaEngine()

        best_move = engine.search(game, depth=2)

        self.assertEqual(best_move.last_move[1], 3)

    def test_min_player_blocks_win(self):
        """
        Verify that the minimizing player (O) chooses a blocking move when X threatens
        to win on the next move.

        Setup
        - Empty board except X tokens at (5,2), (4,2), (3,2) — X threatens column 2.
        - Instantiate game/engine with player="O" and last_move=(3,2).

        Expectation
        - engine.search(game, depth=2) returns a state whose last_move column is 2,
          meaning O blocks the threat.
        """
        board = [[None]*7 for _ in range(6)]

        board[5][2] = "X"
        board[4][2] = "X"
        board[3][2] = "X"

        game = Connect4(board, player="O", last_move=(3, 2))
        engine = AlphaBetaEngine()

        best_move = engine.search(game, depth=2)

        self.assertEqual(best_move.last_move[1], 2)


class TestConnect4ScenarioMinimax(unittest.TestCase):

    def test_two_initial_states_minimax_decisions(self):
        """
        Two small scenarios:

        Scenario A: X has an immediate horizontal win on the bottom row.
        - Board: X at (5,0), (5,1), (5,2). Expect X to play column 3.

        Scenario B: X threatens a vertical win in column 2; O must block.
        - Board: X at (5,2), (4,2), (3,2). Expect O to play column 2.

        Each scenario is run independently and assertions verify the chosen column.
        """
        board_a = [[None]*7 for _ in range(6)]
        board_a[5][0] = "X"
        board_a[5][1] = "X"
        board_a[5][2] = "X"

        engine = AlphaBetaEngine()

        game_a = Connect4(board_a, player="X", last_move=(5, 2))
        best_a = engine.search(game_a, depth=2)
        self.assertEqual(best_a.last_move[1], 3)

        board_b = [[None]*7 for _ in range(6)]
        board_b[5][2] = "X"
        board_b[4][2] = "X"
        board_b[3][2] = "X"

        game_b = Connect4(board_b, player="O", last_move=(3, 2))
        best_b = engine.search(game_b, depth=2)
        self.assertEqual(best_b.last_move[1], 2)


if __name__ == "__main__":
    unittest.main()
