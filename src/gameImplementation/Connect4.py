from __future__ import annotations
from typing import List, Optional
from copy import deepcopy
from src.stateGame.StateGame import StateGame

class Connect4(StateGame):
    """
    Implementación del juego Connect 4 como subclase de StateGame.
    """

    ROWS = 6
    COLS = 7
    PLAYERS = ["X", "O"]

    def __init__(self, board=None, player="X"):
        if board is None:
            board = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.board = board
        self.player = player

    # ---------------------------------------------------------
    #     MÉTODOS QUE IMPLEMENTAN LA INTERFAZ STATEGAME
    # ---------------------------------------------------------

    @classmethod
    def start(cls) -> "Connect4":
        """Retorna un estado inicial con el tablero vacío."""
        return cls()

    def toMove(self) -> str:
        return self.player

    def rival(self, player: str) -> str:
        return "O" if player == "X" else "X"

    def actionResults(self) -> List["Connect4"]:
        if self.isTerminal():
            return []

        states = []
        for col in range(self.COLS):
            row = self._available_row(col)
            if row is not None:
                new_board = deepcopy(self.board)
                new_board[row][col] = self.player
                states.append(Connect4(new_board, self.rival(self.player)))

        return states

    def isTerminal(self) -> bool:
        return self._winner() is not None or self._is_full()

    def heuristicUtility(self, player: str) -> int:
        WIN = 10_000
        winner = self._winner()

        if winner == player:
            return WIN
        elif winner == self.rival(player):
            return -WIN
        else:
            return 0  # heurística neutra para estados no terminales

    def toString(self) -> str:
        s = ""
        for row in self.board:
            s += "| " + " ".join(c if c is not None else "." for c in row) + " |\n"
        s += "  " + " ".join(str(i) for i in range(self.COLS)) + "\n"
        return s

    # ---------------------------------------------------------
    #                   MÉTODOS AUXILIARES
    # ---------------------------------------------------------

    def _available_row(self, col: int) -> Optional[int]:
        """Devuelve la fila libre más baja de una columna."""
        for r in reversed(range(self.ROWS)):
            if self.board[r][col] is None:
                return r
        return None

    def _is_full(self) -> bool:
        return all(self.board[0][c] is not None for c in range(self.COLS))

    # ------------ DETECCIÓN DE GANADOR ---------------------

    def _winner(self) -> Optional[str]:
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for r in range(self.ROWS):
            for c in range(self.COLS):
                player = self.board[r][c]
                if player is None:
                    continue

                for dr, dc in directions:
                    if self._check_line(player, r, c, dr, dc):
                        return player
        return None

    def _check_line(self, player: str, r: int, c: int, dr: int, dc: int) -> bool:
        """Verifica si hay 4 en línea comenzando en (r,c)."""
        for i in range(4):
            rr = r + dr * i
            cc = c + dc * i
            if not (0 <= rr < self.ROWS and 0 <= cc < self.COLS):
                return False
            if self.board[rr][cc] != player:
                return False
        return True
