def linhas():
    print("-" * 28)

# Fica perguntando a idade pro usuário se não digitar um valor inteiro.
linhas()
while True:
    try:
        idade = int(input("Qual sua idade? "))
        if isinstance (idade, int):
            break
        else:
            idade = int(input("Qual sua idade? "))
    except ValueError:
        print("Entrada inválida.")

# Pergunta se tem ingresso até que digite S ou N.
ingresso = str(input("Você tem ingresso? (S/N): ")).lower()
while ingresso not in "sn":
    print("Digite S para sim, N para não.")
    ingresso = str(input("Você tem ingresso? (S/N): ")).lower()

# Verificação final se pode ou não entrar.
while True:
    try:
        if ingresso == "n":
            ingresso = False
        else:
            ingresso = True

        if (idade >= 16) and (ingresso == True):
            print("Pode entrar")
        else:
            print("Não pode entrar")
        linhas()
        # Pergunta se quer continuar o programa. Se sim, reinicia o código.
        continuar = str(input("Verificar novamente? (S/N): ")).lower()
        while continuar not in "sn":
            print("Digite S se tem, N se não tem.")
            continuar = str(input("Verificar novamente? (S/N): ")).lower()
        if continuar == "n":
            linhas()
            break
    except ValueError:
        print("Erro: Entrada inválida.")