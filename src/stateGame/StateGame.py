from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class StateGame(ABC):
    """
    Abstract base class for modeling turn-based, state-driven games.

    This class defines the interface that any game state must implement
    in order to be compatible with generic search algorithms such as
    minimax, alpha-beta pruning, Monte Carlo search, etc.

    A `StateGame` instance represents a *single state* of the game
    and must provide:
      - How to obtain the initial state
      - What actions are possible from this state
      - Whether the state is terminal
      - Which player is to move
      - How to identify the opponent
      - A heuristic evaluation function
      - A human-readable representation of the state
    """

    @classmethod
    @abstractmethod
    def start(cls) -> "StateGame":
        """
        Return the initial state of the game.

        This is typically used to bootstrap search algorithms or
        game simulations.

        Returns:
            StateGame: The initial game state.
        """
        raise NotImplementedError

    @abstractmethod
    def action_results(self) -> List["StateGame"]:
        """
        Return the list of all states reachable by applying
        any legal action from the current state.

        Each resulting state should represent the game after one action
        by the player whose turn it is.

        Returns:
            List[StateGame]: A list of successor states.
        """
        raise NotImplementedError

    @abstractmethod
    def is_terminal(self) -> bool:
        """
        Determine whether the current state is a terminal state.

        A terminal state is one where:
          - the game has ended, and
          - no further moves are allowed.

        Returns:
            bool: True if the state is terminal, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def to_move(self) -> str:
        """
        Return the identifier of the player whose turn it is
        in the current state.

        Returns:
            str: The player who must act next.
        """
        raise NotImplementedError

    @abstractmethod
    def rival(self, player: str) -> str:
        """
        Return the opponent of the given player.

        Args:
            player (str): The player whose opponent is requested.

        Returns:
            str: The rival player.
        """
        raise NotImplementedError

    @abstractmethod
    def heuristic_utility(self, player: str) -> int:
        """
        Evaluate the current state using a heuristic utility function.

        Positive values should favor the given player,
        while negative values should favor the opponent.

        Args:
            player (str): The player for whom the utility is evaluated.

        Returns:
            int: The heuristic score of this state.
        """
        raise NotImplementedError

    @abstractmethod
    def to_string(self) -> str:
        """
        Return a readable, printable string representation
        of the current game state.

        Returns:
            str: A human-friendly description of the state.
        """
        raise NotImplementedError
