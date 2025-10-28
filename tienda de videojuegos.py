# Tienda de videojuegos

info_tienda = ("¡Game On!", 2010)
print("Información de la tienda:", info_tienda)

inventario = {
    "F1 Manager 2024": {"precio": 899, "stock": 5},
    "GTA V": {"precio": 499, "stock": 8},
    "Minecraft": {"precio": 299, "stock": 10}
}

print("\nPrecio del segundo juego (GTA V):", inventario["GTA V"]["precio"])

inventario["F1 Manager 2024"]["stock"] -= 1
print("\nVendiste una copia de F1 Manager 2024.")
print("Stock actualizado:", inventario["F1 Manager 2024"]["stock"])

print("\nInventario actualizado:")
for juego, datos in inventario.items():
    print(f"{juego}: Precio ${datos['precio']}, Stock {datos['stock']}")