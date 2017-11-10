input_1, input_2, input_3 = input().split()

a = float(input_1)
b = float(input_2)
c = float(input_3)

pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * (c**2)
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %0.3f" % triangulo)
print("CIRCULO: %0.3f" % circulo)
print("TRAPEZIO: %0.3f" % trapezio)
print("QUADRADO: %0.3f" % quadrado)
print("RETANGULO: %0.3f" % retangulo)
