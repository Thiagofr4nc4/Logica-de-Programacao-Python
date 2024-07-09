qtd_pokemon = int(input())
pokemons = [qtd_pokemon]
for i in range (qtd_pokemon):
    pokemon, bonus_clima = map(int, input().split())
    print(pokemon + bonus_clima)
   