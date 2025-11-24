# BÚSQUEDA ADVERSARIA

**ESCUELA COLOMBIANA DE INGENIERÍA**

**PRINCIPIOS Y TECNOLOGÍAS IA 2025-2**

## Integrantes
- Andres Felipe Calderon Ramirez - [andrescalderonr](https://github.com/andrescalderonr)
- Santiago Botero Garcia - [LePeanutButter](https://github.com/LePeanutButter)


## LABORATORIO 3/4

**OBJETIVOS**

Desarrollar competencias básicas para:

1.  Modelar y resolver tareas y problemas usando busqueda adversaria
2.  Desarrollar módulos y lógica de juegos (*Game Theory*)
3.  Implementar busqueda adversaria, específicamente MiniMax

**ENTREGABLE**

*Reglas para el envío de los entregables*:

-   **Forma de envío:** Este laboratorio se debe enviar únicamente a
    través de la plataforma Moodle en la actividad definida. Se tendrán
    dos entregas: inicial y final.

-   **Formato de los archivos:** Incluyan en un archivo *.zip* los
    archivos correspondientes al laboratorio.

-   **Nomenclatura para nombrar los archivos:** El archivo deberá ser
    renombrado, "AdvSearch-lab-" seguido por los usuarios
    institucionales de los autores ordenados alfabéticamente (por
    ejemplo, se debe adicionar pedroperez al nombre del archivo, si el
    correo electrónico de Pedro Pérez es
    <pedro.perez@mail.escuelaing.edu.co>)

# **IMPLEMENTACIÓN DE BÚSQUEDA ADVERSARIA: MINIMAX PODA $\alpha$ - $\beta$**

**Para este apartado se va a implementar la lógica de juego, bajo regla
de dos jugadores, y su la decisión de la mejor acción dada por el
algoritmo de Búsqueda MiniMax optimizado con $\alpha$ - $\beta$**.

*La historia de la teoría de juegos tiene sus raíces en la estrategia
matemática y económica, siendo el teorema minimax de John von Neumann
(1928) un momento crucial que la estableció como un campo formal.
MiniMax es un algoritmo de toma de decisiones utilizado en juegos por
turnos para dos jugadores, como el tres en raya, el ajedrez y las damas.
Está diseñado para encontrar el movimiento óptimo para un jugador,
suponiendo que el oponente también juega de forma óptima.*

*Este algoritmo asume que hay dos jugadores. Un jugador actúa como MAX y
el segundo como MIN. MAX maximizará sus propias posibilidades de ganar
(puntos o recompensa, es decir, elegirá el mejor movimiento). MIN
minimizará las posibilidades de ganar del oponente (puntos o recompensa,
es decir, elegirá el peor movimiento).*

![](img/diagram_class.png)

``` python
from abc import ABC, abstractmethod
from __future__ import annotations
```

## PARTE I. IMPLEMENTACIÓN DE UN JUEGO CON DOS JUGADORES

Implementar un juego para dos jugadores (ambos agentes) del tipo de
turnos o estados (teniendo en cuenta la clase *StateGame*).

### GAME THEORY: JUEGO DE ESTADOS

``` python
class StateGame(ABC):
  """ Abstracta: define los métodos clave para modelar cualquier juego por turnos (representados en estados)
  """


  @classmethod
  def start() -> StateGame:
    """ Iniciar el juego
    Args:
    Returns:
       el estado inicial del juego
    """
    pass

  def actionResults() -> list:
    """ Devuelve los próximos estados correspendientes a los movimientos legales del estado actual
    Args:
    Return:
      listado de estados del juego
    """
    pass
  def isTerminal() -> bool:
    """ Evaluar el estado actual, si es un estado que corresponde al fin del jusgo
    Args:
    Returns:
       valor de verdad a la proposición "es un estado meta?"
    """
    pass
  def toMove() -> str:
    """ Define que jugador tiene el turno en el estado actual
    Args:
    Returns:
       identificador del jugador
    """
    pass
  def rival(player: str) -> str:
    """ Define que jugador es el rival del jugador player
    Args:
      player : identificador de un jugador
    Returns:
       identificador del jugador rival
    """
    pass
  def heuristicUtility(player: str): int
    """ Establecer el criterio (heuristica) de utilidad del jugador
    Args:
      player : identificador del jugador
    Returns:
      valor de utilidad
    """
    pass
  def toString() -> str
    """ Muestra el estado del juego en formato de cadena
    Args:
    Returns:
      estado del juego
    """
    pass
```

Para el juego simple propuesto por su profesor, implemente la clase que
lo modela considerando la especificación dada.

``` python
# Implementar la clase abstracta y documentar los métodos implementados
```

## PARTE II. IMPLEMENTACIÓN DE BÚSQUEDA: MINIMAX $\alpha$ - $\beta$

Implementar la lógica de búsqueda adversaria para que el jugador tome
una decisión y generé una acción (la mejor posible)

### BÚSQUEDA ADVERSARIA: MINIMAX PODA $\alpha$ - $\beta$

``` python
class AlphaBetaEngine():
  """ Algoritmo de búsqueda adversaria MiniMax con poda (optimización) por AlphaBeta
  """
  def search(s: StateGame, depth: int) -> StateGame:
    """ Generar mejor acción/transición del juego a partir de un estado
    Args:
       s : estado de juego
       depth : profundidad de búsqueda deseada
    Returns:
       siguiente estado decidido
    """
    pass

  def maxValue(s: StateGame, depth: int, alpha: int, beta: int) -> int:
    """ Evaluar valor para MAX
    Args:
       s : estado de juego
       depth : profundidad de búsqueda deseada
       alpha : valor de criterio alfa
       alpha : valor de criterio beta
    Return:
      valor calculado para MAX
    """
    pass
  def minValue(s: StateGame, depth: int, alpha: int, beta: int) -> int:
    """ Evaluar valor para MIN
    Args:
       s : estado de juego
       depth : profundidad de búsqueda deseada
       alpha : valor de criterio alfa
       alpha : valor de criterio beta
    Returns:
       valor calculado para MIN
    """
    pass
```

``` python
# A partir de dos posibles estados iniciales, pruebe el desarrollo del juego y las decisiones por heurisrica MiniMax
```

## RETROSPECTIVA

**1.** ¿Cuál fue el tiempo total invertido en el laboratorio por cada
uno de ustedes? (Horas/Hombre)

**2.** ¿Cuál es el estado actual del laboratorio? ¿Por qué?

**3.** ¿Cuál consideran fue el mayor logro? ¿Por qué?

**4.** ¿Cuál consideran que fue el mayor problema técnico? ¿Qué hicieron
para resolverlo?

**5.** ¿Qué hicieron bien como equipo? ¿Qué se comprometen a hacer para
mejorar los resultados?

**6**.¿Qué referencias usaron? ¿Cuál fue la más útil? Incluya citas con
los estándares adecuados.

*Incluyan las respuesta*
