# Importamos clases
from Empleado import Empleado
from Operario import Operario
from Oficial import Oficial
from Directivo import Directivo
from Tecnico import Tecnico

# Función principal
def main():
    # Creamos empleado
    emp = Empleado("Rafa")
    print(emp)

    # Creamos operario
    oper = Operario("Alfonso")
    print(oper)

    # Creamos directivo
    manag = Directivo("Mario")
    print(manag)

    # Creamos oficial
    oficial = Oficial("Luis")
    print(oficial)

    # Creamos técnico
    tech = Tecnico("Pablo")
    print(tech)

# Ejecutamos si es main
if __name__ == "__main__":
    main()