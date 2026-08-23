vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

def calcular(vitorias, derrotas):

    saldo = vitorias - derrotas
    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias >= 11 and vitorias <= 20:
        nivel = "Bronze"
    elif vitorias >= 21 and vitorias <= 50:
        nivel = "Prata"
    elif vitorias >= 51 and vitorias <= 80:
        nivel = "Ouro"
    elif vitorias >= 81 and vitorias <= 90:
        nivel = "Diamante"
    elif vitorias >= 91 and vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    return  saldo, nivel

resultado = calcular(vitorias, derrotas)

print(f"O Herói tem de saldo de {resultado[0]} está no nível de {resultado[1]}")


#