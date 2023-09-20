# QUARTA VERSÃO ## COMPACTADASSO
(lambda n = int(input()) : [print(*[("*" + ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:n][::-1]))[max(abs(i - n), abs(j - n))] + "" for j in range(2 * n + 1)]) for i in range(2 * n + 1)])()





# TERCEIRA VERSÃO ## Em 3 linhas
# n = int(input())
# letras, tam = "*" + ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:n][::-1]), 2 * n + 1
# [print(*[letras[max(abs(i - n), abs(j - n))] + "" for j in range(tam)]) for i in range(tam)]





# SEGUNDA VERSÃO ## Sem funções separadas
# n: int = int(input())
# letras: str = "*" + ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:n][::-1])
# tam: int = 2 * n + 1

# for i in range(tam):
#     linha: str = ""
#     for j in range(tam):
#         linha += letras[max(abs(i - n), abs(j - n))] + " "
#     print(linha)





# PRIMEIRA VERSÃO ## Legivel e organizado
# n: int = int(input())
# letras: str = "*" + ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:n][::-1])
# tam: int = 2 * n + 1

# def Dist(posX: (int, int), posY: (int, int)) -> int:
#     return max(abs(posX[0] - posY[0]), abs(posX[1] - posY[1]))

# def Pegar(posX: (int, int)) -> str:
#     return letras[Dist(posX, (n, n))]

# for i in range(tam):
#     linha: str = ""
#     for j in range(tam):
#         linha += Pegar((i, j)) + " "
#     print(linha)
