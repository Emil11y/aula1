n1 = int(input("insira n1 :"))
n2 = int(input("insira n2 :"))
n3 = int(input("insira n3 :"))
if n1 > n2 and n1 > n3:
    print (f"o maior numero é: {n1} ")
elif n2 > n3 and n2 >n1:
    print (f"o maior é:{n2}")
else:
    print(f"o maior é: {n3}")
