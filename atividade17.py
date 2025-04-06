vogais="a e i o u A E I O U"
num_vogais=0
palavra=input("Digite uma palavra: ")

for letra in palavra:
    if letra in vogais:
        num_vogais += 1
        
if num_vogais > 0:
    print(f"A palavra '{palavra}' tem {num_vogais} vogais.")
else:
    print("Não há vogais na palavra.")
