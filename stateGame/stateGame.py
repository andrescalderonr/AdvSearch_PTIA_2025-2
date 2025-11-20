from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class StateGame(ABC):
    """
    Clase abstracta para modelar juegos por turnos basados en estados.
    """

    @classmethod
    @abstractmethod
    def start(cls) -> "StateGame":
        """Devuelve el estado inicial del juego."""
        pass

    @abstractmethod
    def actionResults(self) -> List["StateGame"]:
        """Devuelve los estados alcanzables desde el estado actual."""
        pass

    @abstractmethod
    def isTerminal(self) -> bool:
        """Indica si el estado actual es terminal."""
        pass

    @abstractmethod
    def toMove(self) -> str:
        """Devuelve el jugador al que le corresponde mover."""
        pass

    @abstractmethod
    def rival(self, player: str) -> str:
        """Devuelve el jugador rival."""
        pass

    @abstractmethod
    def heuristicUtility(self, player: str) -> int:
        """Calcula la utilidad heurística del estado."""
        pass

    @abstractmethod
    def toString(self) -> str:
        """Retorna una representación legible del estado."""
        pass
