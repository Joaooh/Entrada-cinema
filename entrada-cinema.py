def linhas():
    print("-" * 28)

while True:
    linhas()
    idade = int(input("Qual sua idade? "))
    while idade <= 0:
        print("Entrada inválida.")
        idade = int(input("Qual sua idade? "))

    ingresso = str(input("Você tem ingresso? (S/N): ").lower())
    while ingresso[:1] != "s" and ingresso[:1] != "n":
        ingresso = str(input("Você tem ingresso? (S/N): ").lower())

    if ingresso == "s":
        ingresso = True
    else:
        ingresso = False

    if (idade >= 16) and (ingresso == True):
        print("\nPode entrar!")
    else:
        print("\nNão pode entrar.")
    linhas()

    continuar = str(input("Verificar novamente? (S/N): ").lower())
    while continuar[:1] != "s" and continuar[:1] != "n":
        continuar = str(input("Verificar novamente? (S/N): ").lower())

    if continuar == "n":
        break
