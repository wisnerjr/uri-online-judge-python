input_1 = input()

values = [int(x) for x in input_1.split()]

a = values[0]
b = values[1]
c = values[2]

maiorAB = (a + b + abs(a - b)) / 2

maiorValor = (maiorAB + c + abs(maiorAB - c)) / 2

# metodo mais simples
# maiorValor = max(values)


print("%i eh o maior" % maiorValor)
