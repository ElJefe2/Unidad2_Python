''' Jose Antonio Garcia Martinez  1218100524'''
import random

class Mayor_menor:
   def may_men(self):
      self.num1=0
      self.num2=""
      num1=random.choice(range(1000))
      num2 = int(input("Introduce un número del 1 al 1000: "))
      if(num1>num2):
         print("El numero Ingresado es menor al numero generado ")
         print("Numero mayor "+str(num1))
         print("Numero menor "+str(num2))
      elif(num1<num2):
         print("El numero generado "+str(num1)+" es menor al numero Ingresado "+str(num2))
         print("Numero mayor "+str(num2))
         print("Numero menor "+str(num1))
      else:
         print("Los numeros son iguales")
maymen=Mayor_menor()
maymen.may_men()
      
