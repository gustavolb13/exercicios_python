valor_por_hora = input("Quanto você ganha por hora? ")
horas_trabalhadas = input("Horas trabalhadas no mês: ")
valor_por_hora, horas_trabalhadas = float(valor_por_hora), float(horas_trabalhadas)
salario = horas_trabalhadas * valor_por_hora
print(f"O salário desse mês é {salario:.2f}")