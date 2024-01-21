pi  = 3.14159265
raio = input("Digite o raio: ")
raio_em_real = float(raio)
area_do_circulo = pi * raio_em_real**2 # expoentes são realizados primeiro que operações de multiplicação
print(f"A área do circulo é igual a {area_do_circulo:.2f}")