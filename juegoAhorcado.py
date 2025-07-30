#El objetivo consiste en desarrollar el juego interactivo “adivina la palabra”. 
#El funcionamiento esperado es el siguiente:
#Al ejecutar el programa se mostrará por pantalla una palabra oculta usando tantos guiones como
#letras contiene la palabra a adivinar(la palabra a adivinar será elegida por el programa usando el módulo de Python random), 
#la cantidad de vidas con las que cuenta el jugador y las cantidad de letras incorrectas que va ingresando.
#Cuando el jugador ingresa una letra es necesario que se valide el dato (que sea una letra).
#Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a alguna de las letras de la palabra a adivinar.
#Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se restará una vida.
#El juego finaliza cuando el jugador queda sin vidas, cuando adivina todas las letras de la palabra o 
#cuando selecciona no jugar más. Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si perdió.
import random

print("Bienvenido al juego adivinando la palabra 😊")

Imagenes = ["🤦‍♂️","😒","😢","😣","😵","☠️","👻"]

Palabras = ["mesa", "lámpara", "cuaderno", "taza", "bolígrafo", "silla", "computadora"]

def palabraRandom():
    p = random.randint(0,len(Palabras)-1)
    return Palabras[p]

def esconderPalabra ():
  palabra = palabraRandom()
  ocultarPalabra = ["*"]*len(palabra)
  return ocultarPalabra

vidas = 0 

def juego (ocultarPalabra, vidas):
   print (Imagenes[vidas])
   print ('')
   print(ocultarPalabra)


# En esta seccion voy a proponer la estructura del while para determinar la validez de la 
# palabra y si corresponde a una respuesta correcto en el juego. 
   