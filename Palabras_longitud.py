''' Jose Antonio Garcia Martinez  1218100524'''
class longitud:
  def long(self):
    letra=input("Ingrese una palabra: ")
    num=letra.lower()
    num=num[0].upper()+num[1:]
    numletra=0
    for i in letra:
      numletra+=1
    print('Su palabra ' , num , 'tiene',numletra,'letras')
cadena=longitud()
cadena.long()
