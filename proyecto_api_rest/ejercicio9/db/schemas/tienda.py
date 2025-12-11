# Función para transformar una sola tienda en formato diccionario
def tienda_schema(tienda) -> dict:
    return {"id": str(tienda["_id"]),
            "domicilio": tienda["domicilio"],
            "telefono": tienda["telefono"],
            "precio_alquiler": tienda["precio_alquiler"],
}

# Función para transformar una lista de tiendas
def tiendas_schema(tiendas) -> list:
    return [tienda_schema(tienda) for tienda in tiendas]