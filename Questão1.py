idade_doador = input("Qual a sua idade? ")
idade_doador = int(idade_doador)

if idade_doador < 16:
    print("Impedimento: menor de 16 anos.")
elif idade_doador > 69:
    print("Impedimento: maior de 69 anos.")
elif idade_doador == 16 or idade_doador < 18:
    print("Restrição: requer autorização do responsável.")
elif idade_doador == 60 and idade_doador < 69:
    print(" Restrição: não pode ser a primeira doação.")
elif idade_doador == 18 or idade_doador < 60:
    print("Sem impedimentos ou restrições.")