n1=int(input("ingrese un numero\n"))
n2=int(input("ingrese otro numero\n"))
n3=int(input("ingrese un numero\n"))
if(n1 > n2 and n1 > n3):
 print("El numero Maximo es " + str(n1))
else:
 if(n2 > n1 and n2 > n3):
  print("El numero Maximo es " + str(n2))
 else:
  print("El numero Maximo es " + str(n3))
  
 input()