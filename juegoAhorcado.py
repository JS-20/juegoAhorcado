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
# comenzamos con un msj para el usuario
print(" ")
print("¡Bienvenido al juego: Adivinando la palabra!")
# Aca hice dos listas para poder usarlas en el juego
Imagenes = ["😊","😒","😢","😣","😵","☠️","👻"]

Palabras = ["mesa", "lampara", "cuaderno", "taza", "bolígrafo", "silla", "computadora"]
#Con randon elijo una palabra de la lista
palabra = random.choice(Palabras)
#Con esta variable mas la funcion ocultamos la palabra
ocultarPalabra = ["-"]*len(palabra)
#inicio la variable de vidas
v = 6
#En esta lista ponemos las letras incorrectas que ingreso el usuario, para poder mostrar el conteo
letrasIncorrectas = []
#defenimos esta funcion para poder mostrar las caracteristicas del juego
def juego():
   print(" ")
   print(Imagenes[6-v])
   print('')
   print("palabra: " + " ".join(ocultarPalabra))
   print('')
   print("❤️ "+" " +str(v))
   print('')
   print("❌ cantidad de letras incorrectas: " + str(len(letrasIncorrectas)))
   print('')
#Realizamos el bucle para que se pueda pueda mostrar el juego y que tenga en cuenta la logica
while  v > 0 and "-" in ocultarPalabra: 
   juego()
   #el usuario ingresa la letra y verificamos si es una letra
   letra = input("✍️  ingresa una letra para adivinar la palabra: ").lower()
   print(" ")
   if not letra.isalpha() or len(letra) != 1:
      print("❌  por favor ingrese solo una letra del abecedario")
      letrasIncorrectas.append(letra)
      v -= 1
      continue
   #verificamos si la letra ingresada pertenece a la palabra
   if letra in palabra: 
      for i in range(len(palabra)):
         if palabra[i]==letra:
            ocultarPalabra[i] = letra
            print("🎉 ¡Bien! la letra esta en la palabra ")
            print(" ")
# Aca se restara una vida por letra que o este en la palabra
   else:
      letrasIncorrectas.append(letra)
      v -= 1
      print(" ")
      print("❌  esa letra no esta en la palabra")
      print(" ")
      print("Te quedan " + str(v) + " vidas ❤️")
      print(" ")
# si el usuariose queda sin vidas o logra ganar se verificara con este if
if "-" in ocultarPalabra:
      print(" ")
      print("❌ te quedaste sin intentos. La palabra era "+ " ".join(palabra))
      print(" ")
else: 
      print(" ") 
      print("🎉  felicitaciones adivinaste la palabra: "+ " ".join(palabra))
      print(" ")
