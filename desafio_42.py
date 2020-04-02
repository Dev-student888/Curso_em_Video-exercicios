# Refaça o desafio 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
#
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-' * 60)
print('-' * 24, 'DESAFIO 42', '-' * 24)
print('-' * 60)
a = str(input('Digite o comprimento de uma reta qualquer: ')).strip()
b = str(input('Digite o comprimento de outra reta qualquer: ')).strip()
c = str(input('Digite o comprimento de outra reta qualquer: ')).strip()

a = float(a[:1]) if ' m' in a or 'm' in a else float(a[:3])
b = float(b[:1]) if ' m' in b or 'm' in b else float(b[:3])
c = float(c[:1]) if ' m' in c or 'm' in c else float(c[:3])

if abs(b) - abs(c) < a < b + c and abs(a) - abs(c) < b < a + c and abs(a) - abs(b) < c < a + b:
    if a == b == c:
        print('Estas retas podem formar um triângulo Equilátero!')
    elif a == b or a == c or b == c:
        print('Estas retas podem formar um triângulo Isósceles!')
    elif a != b != c != a:
        print('Estas retas podem formar um triângulo Escaleno!')
else:
    print('Sinto Muito! Mas essas retas não podem formar um triangulo!')
