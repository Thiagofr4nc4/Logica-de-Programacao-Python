base_piramide = int(input("Digite a altura da pirâmide: "))

for i in range(1, base_piramide + 1):
    espacos = ">" * (base_piramide - i)
    blocos = "#" * i
    linha = espacos + blocos
    print(linha)
