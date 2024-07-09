familiares, bolinhas_dadas = map(int, input().split())
total_bolinhas = 0
bolinhas = bolinhas_dadas

for i in range(1, familiares +1):
    total_bolinhas += bolinhas
    bolinhas *= 2
print(total_bolinhas)