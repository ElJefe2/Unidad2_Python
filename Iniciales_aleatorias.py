''' Jose Antonio Garcia Martinez  1218100524'''
import random

class aleatori():
   def aleatorio(self):
      num = int(input("Introduce un número: "))
      i=0
      while(i<num):
         num2 = random.choice(range(1000))
         print(num2)
         i=i+1

al=aleatori()
al.aleatorio()
      
