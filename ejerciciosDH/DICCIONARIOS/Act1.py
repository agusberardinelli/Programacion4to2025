#Crear una variable llamada auto1 y, dentro de ella, guardar un diccionario con al menos tres propiedades (color, cantidad_puertas, marca).
#Repetir el paso anterior, pero replicando la estructura de datos para las variables auto2, auto3 y auto4.
#A través de la notación de corchetes, modificar el color del auto2 y luego mostrarlo por consola.


auto1 = {
  "color" : "azul",
  "cantidad_puertas" : "4",
  "marca" : "toyota"
} 

auto2 = {
  "color" : "blanco",
  "cantidad_puertas" : "2",
  "marca" : "nissan"
} 

auto3 = {
  "color" : "Negro",
  "cantidad_puertas" : "6",
  "marca" : "audi"
} 

auto4 = {
  "color" : "Rojo",
  "cantidad_puertas" : "3",
  "marca" : "ferrari"
} 

auto2["color"] = "blanco"
 
print(auto2["color"])
