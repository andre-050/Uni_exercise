# Problema 3 - Inventario de Almacén

Este proyecto implementa una herramienta sencilla para auditar el inventario de un almacén y determinar qué artículos deben reabastecerse.

## Descripción

Se trabaja con una matriz donde cada registro contiene:
- Código del artículo
- Nombre del artículo
- Stock actual
- Stock mínimo requerido

La aplicación recorre la matriz y utiliza una función para calcular la cantidad exacta a pedir por artículo.

## Reglas de negocio

- Si el `Stock Actual` es menor que el `Stock Mínimo Requerido`, se solicita la diferencia: `Stock Mínimo Requerido - Stock Actual`.
- Si el `Stock Actual` es mayor o igual al `Stock Mínimo Requerido`, no se pide nada (`0`).

## Salida esperada

Se imprime una lista de pedidos con el nombre del artículo y la cantidad exacta que debe solicitarse.

## Estructura de la matriz

Cada elemento de la matriz tiene la forma:
`[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]`

## Ejemplo de datos

- Arroz
- Aceite
- Azúcar
- Lentejas
- Sal
