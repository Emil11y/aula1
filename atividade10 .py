idade = int(input("insira sua idade:"))
if idade <12:
    print ("criança")
elif idade >= 12 and idade <= 17: 
    print ("adolescente")
elif idade >= 18 and idade == 59:
    print ("adulto")
else:
    print ("idoso")