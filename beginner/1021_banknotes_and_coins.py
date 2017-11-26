value = float(input())
value_aux = value
banknotes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
total_banknotes = []
total_coins = []

value += 0.001

for banknote in banknotes:
    division = value // banknote
    total_banknotes.append(division)
    value = value % banknote

for coin in coins:
    division = value // coin
    total_coins.append(division)
    value = value % coin

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % total_banknotes[0])
print("%i nota(s) de R$ 50.00" % total_banknotes[1])
print("%i nota(s) de R$ 20.00" % total_banknotes[2])
print("%i nota(s) de R$ 10.00" % total_banknotes[3])
print("%i nota(s) de R$ 5.00" % total_banknotes[4])
print("%i nota(s) de R$ 2.00" % total_banknotes[5])

print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % total_coins[0])
print("%i moeda(s) de R$ 0.50" % total_coins[1])
print("%i moeda(s) de R$ 0.25" % total_coins[2])
print("%i moeda(s) de R$ 0.10" % total_coins[3])
print("%i moeda(s) de R$ 0.05" % total_coins[4])
print("%i moeda(s) de R$ 0.01" % total_coins[5])