x= int(input('Digite um numero5: '))
y= int(input('Digite outro numero: '))
z= str(input('insira uma tipo de operação:'))
if z== "+":
   print(f"resultado:{x+y}")
elif z=="-":
   print(f"resultado:{x-y}")
elif z =="*":
   print(f"resultado:{x*y}")
else:
   print(f"resultado:{x/y}")