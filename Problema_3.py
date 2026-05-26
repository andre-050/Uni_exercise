# Fase 5 - Evaluación Final POA
# Nombre del estudiante: Andrea Natalia Osorio Largo
# Grupo: 213022A_2201
# Programa: Ingenieria en Sistemas
# Código Fuente: Andrea_Osorio

# Problema 3: Inventario de Almacén 
# Matriz: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    [1, "Arroz", 10, 20],
    [2, "Aceite", 5, 15],
    [3, "Azúcar", 30, 25],
    [4, "Lentejas", 8, 12],
    [5, "Sal", 18, 18]
]

# Función para calcular la cantidad exacta a pedir
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Imprimir lista de pedidos
print("LISTA DE PEDIDOS")
print("----------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

    print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")