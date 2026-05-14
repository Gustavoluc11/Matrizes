# matriz = [
#     [1,0,0,0,0],
#     [0,1,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,1,0],
#     [0,0,0,0,1],
# ]
#
# for linha in matriz:
#     print(linha)
###################################################
# matriz = []
#
# maior = None
# linha_maior = 0
# coluna_maior = 0
#
# # Ler a matriz
# for i in range(4):
#     linha = []
#
#     for j in range(4):
#         valor = int(input(f"Digite o valor [{i}][{j}]: "))
#         linha.append(valor)
#
#         # Verifica o maior valor
#         if maior is None or valor > maior:
#             maior = valor
#             linha_maior = i
#             coluna_maior = j
#
#     matriz.append(linha)
#
# # Mostrar matriz
# print("\nMatriz:")
#
# for linha in matriz:
#     print(linha)
#
# # Resultado
# print("\nMaior valor:", maior)
# print("Linha:", linha_maior)
# print("Coluna:", coluna_maior)
#######################################################################
# matriz = []
#
# maior_nota = 0
# matricula_maior = 0
#
# for i in range(5):
#     linha = []
#
#     matricula = int(input("Digite a matrícula: "))
#     provas = int(input("Digite a média das provas: "))
#     trabalhos = int(input("Digite a média dos trabalhos: "))
#
#     nota_final = provas + trabalhos
#
#     linha.append(matricula)
#     linha.append(provas)
#     linha.append(trabalhos)
#     linha.append(nota_final)
#
#     matriz.append(linha)
#
#     if nota_final > maior_nota:
#         maior_nota = nota_final
#         matricula_maior = matricula
#
# print("\nMatriz:")
#
# for linha in matriz:
#     print(linha)
#
# print("\nMatrícula do aluno com maior nota final:", matricula_maior)