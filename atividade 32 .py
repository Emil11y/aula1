semana = []

for dia in range(7):
    temp = float(input(f"Insira a temperatura do dia {dia + 1}: "))
    semana.append(temp)

maior = max(semana)
menor = min(semana)
media = sum(semana) / len(semana)

acima_da_media = []
for i in range(7):
    if semana[i] > media:
        acima_da_media.append(i + 1)

print(f"Maior temperatura foi: {maior}°C")
print(f"Menor temperatura foi: {menor}°C")
print(f"Média semanal é: {media}°C")
print(f"Dias com temperatura acima da média são: ")
for dia in acima_da_media:
    print(f"dia {dia}")


    
