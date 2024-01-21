altura = input("Altura: ")
comprimento =  input("Comprimento: ")
altura, comprimento = float(altura), float(comprimento)
area_do_quadrado = altura * comprimento
valor_em_dobro_da_area = area_do_quadrado * 2
print(f"O dobro da área desse quadrado é {valor_em_dobro_da_area}")