''' Jose Antonio Garcia Martinez  1218100524'''
import math

class par_inpar:
   def numeros(self):
      self.numero = 0
      numero = input("Introduce un número: ")
      numero = int(numero)
      if numero == 0:
          print ("Este número es par.")
      elif numero%2 == 0:
          print ("Este numero es par")
      else:
          print ("Este numero es impar")
num = par_inpar()
num.numeros()
         
