areas_analisadas = int(input())
grau_areas = 0

for i in range(1, areas_analisadas + 1):
    grau_areas += int(input())

percentual_oleo = (grau_areas / areas_analisadas) * 100


if percentual_oleo < 30:
    print("Regiao segura")
elif percentual_oleo >= 30 and percentual_oleo <= 50:
    print("Regiao em estado de alerta")
else:
    print("Regiao com alto indice de perda de biodiversidade")