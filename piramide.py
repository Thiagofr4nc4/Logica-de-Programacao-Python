altura_piramide = int(input())
for i in range(1, altura_piramide + 1):
    espacos = " " * (altura_piramide - i)
    numeros = str(i) * (2 * i - 1)
    print(espacos + numeros)