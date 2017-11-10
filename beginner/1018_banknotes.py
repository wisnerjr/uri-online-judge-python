value = int(input())
value_aux = value
banknotes = [100, 50, 20, 10, 5, 2, 1]
total_banknotes = []

for banknote in banknotes:
    division = value // banknote
    total_banknotes.append(division)
    value = value % banknote

print(value_aux)
print("%i nota(s) de R$ 100,00" % total_banknotes[0])
print("%i nota(s) de R$ 50,00" % total_banknotes[1])
print("%i nota(s) de R$ 20,00" % total_banknotes[2])
print("%i nota(s) de R$ 10,00" % total_banknotes[3])
print("%i nota(s) de R$ 5,00" % total_banknotes[4])
print("%i nota(s) de R$ 2,00" % total_banknotes[5])
print("%i nota(s) de R$ 1,00" % total_banknotes[6])