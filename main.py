from travel import Travel
from bariloche import Bariloche
from cancun import Cancun
from dbsqlite import Datos



travel_option = input("Elija el viaje que quiera realizar Cancun o Barilloche: ")
person_cant = int(input("Ingrese la cantidad de personas que viajaran: "))
days_cant = int(input("Ingrese los dias para su viaje: "))

viaje = Travel()
bariloche = Bariloche()
cancun = Cancun()
dato = Datos()

viaje.setPerson(person_cant)
viaje.setDays(days_cant)

if travel_option == "bariloche":
    price = bariloche.discount(person_cant,days_cant)
        
    
elif travel_option == "cancun":
    price = cancun.discount(person_cant,days_cant)

else:
        print("El viaje seleccionado no existe o lo escribio de forma incorrecta")

    #Save date in database
save = dato.insert(travel_option,person_cant,days_cant,price)
print(save)

def comprobante(self):
        pass

