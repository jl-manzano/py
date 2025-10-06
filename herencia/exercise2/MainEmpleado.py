from Empleado import Empleado
from Operario import Operario
from Oficial import Oficial
from Directivo import Directivo
from Tecnico import Tecnico

def main():
    emp = Empleado("Rafa")
    print(emp)

    oper = Operario("Alfonso")
    print(oper)

    manag = Directivo("Mario")
    print(manag)

    oficial = Oficial("Luis")
    print(oficial)

    tech = Tecnico("Pablo")
    print(tech)

if __name__ == "__main__":
    main()