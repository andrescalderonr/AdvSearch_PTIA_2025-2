from src.gameImplementation import Connect4

game = connect4.start()

print("Estado inicial:")
print(game.toString())

# Obtener movimientos posibles
next_states = game.actionResults()
print("Cantidad de movimientos posibles:", len(next_states))

# Mostrar un movimiento de ejemplo
print("\nPrimer movimiento posible:")
print(next_states[0].toString())
