nota1 = input("Nota de português: ")
nota2 = input("Nota de matemática: ")
nota3 = input("Nota de física: ")
nota4 = input("Nota de história: ")
nota1, nota2, nota3, nota4 = float(nota1), float(nota2), float(nota3), float(nota4)
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média bimestral é {media:.2f}")