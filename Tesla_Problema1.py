bateria = int(input("Qual a percentagem de bateria? "))

if bateria < 0 or bateria > 100:
    print("Percentagem inválida")

elif bateria >= 80:
    print("Bateria suficiente")

elif bateria >= 30:
    print("Recomenda-se carregar")

else:
    print("Bateria baixa! Carregar urgentemente")