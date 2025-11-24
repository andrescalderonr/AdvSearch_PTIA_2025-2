from __future__ import annotations
from src.stateGame.StateGame import StateGame

class AlphaBetaEngine:
    """
    Minimax adversarial search algorithm with Alpha-Beta pruning.

    This class is designed to be used as a mixin: its methods expect
    `self` to be a `StateGame` instance. The game state provides:
      - available successor states,
      - terminal state detection,
      - turn information,
      - heuristic utility evaluation.
    """

    def search(self, s: StateGame, depth: int) -> StateGame:
        """
        Compute the best next state from the current one using Minimax
        with Alpha-Beta pruning.

        Args:
            s (StateGame): Current game state.
            depth (int): Maximum search depth.

        Returns:
            StateGame: The selected successor state.
        """

        best_state = None
        best_value = float("-inf")
        inf = 10 ** 9
        alpha, beta = -inf, inf

        for child in s.action_results():
            value = self.min_value(child, depth - 1, alpha, beta)
            if value > best_value:
                best_value = value
                best_state = child

            alpha = max(alpha, best_value)

        return best_state

    def max_value(self, s: StateGame, depth: int, alpha: int, beta: int) -> int:
        """
        Compute the value of a MAX node (player to maximize utility).

        Args:
            s (StateGame): Current game state.
            depth (int): Remaining search depth.
            alpha (int): Alpha pruning parameter.
            beta (int): Beta pruning parameter.

        Returns:
            int: The best utility value MAX can secure.
        """
        if depth == 0 or s.is_terminal():
            return s.heuristic_utility(s.to_move())

        value = float("-inf")

        for child in s.action_results():
            value = max(value, self.min_value(child, depth - 1, alpha, beta))
            alpha = max(alpha, value)

        if value >= beta:
            return value

        return value

    def min_value(self, s: StateGame, depth: int, alpha: int, beta: int) -> int:
        """
        Compute the value of a MIN node (opponent of current player).

        Args:
          s (StateGame): Current game state.
          depth (int): Remaining search depth.
          alpha (int): Alpha pruning bound.
          beta (int): Beta pruning bound.

        Returns:
          int: The best utility value MIN can secure (minimizing).
        """
        if depth == 0 or s.is_terminal():
            opponent = s.rival(s.to_move())
            return s.heuristic_utility(opponent)

        value = float("inf")

        for child in s.action_results():
            value = min(value, self.max_value(child, depth - 1, alpha, beta))
            beta = min(beta, value)

        if value <= alpha:
            return value

        return value