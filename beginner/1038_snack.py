table = {"1" : 4.00, "2" : 4.50, "3" : 5.00, "4" : 2.00, "5" : 1.50}

key = input().split()

aux = key[0]

total = table[aux] * float(key[1])

print("Total: R$ %.2f" % total)