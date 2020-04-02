# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# print('A hipotenusa vai medir {:.2f}'.format((co**2+ca**2)**(1/2)))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
