# Importamos clase Punto
from Punto import Punto

<<<<<<< HEAD
# Creamos dos puntos
p1 = Punto(3, 4)
p2 = Punto(0, 0)

# Mostramos los puntos
print(p1)
print(p2)

# Mostramos distancia entre p1 y p2
print("Distance:", p1.distancia(p2))

# Desplazamos p1
p1.desplaza(1, -1)
print(p1)

# Reasignamos coordenadas a p1
p1.setXY(7, -5)
print(p1)

# Distancia actualizada con p2
print("Distance:", p1.distancia(p2))

# Desplazamos p2
p2.desplaza(1, 2)
print(p2)

# Nueva distancia
print("Distance:", p1.distancia(p2))

# Reasignamos coordenadas a p2
p2.setXY(-2, 6)
print(p2)

# Última distancia
print("Distance:", p1.distancia(p2))
=======
def main():
    p1 = Punto(3, 4)
    p2 = Punto(0, 0)

    print(p1)
    print(p2)

    print("Distance:", p1.distancia(p2))
    p1.desplaza(1, -1)
    print(p1)

    p1.setXY(7, -5)
    print(p1)
    print("Distance:", p1.distancia(p2))

    p2.desplaza(1, 2)
    print(p2)
    print("Distance:", p1.distancia(p2))

    p2.setXY(-2, 6)
    print(p2)
    print("Distance:", p1.distancia(p2))

main()
>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
