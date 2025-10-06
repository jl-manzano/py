from Punto import Punto

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