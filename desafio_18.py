from math import sin, cos, tan, trunc, radians
print('=' * 10, 'DESAFIO 18', '=' * 10)
angulo = float(input('Digite algum ângulo: '))
print('O ângulo digitado foi {}°'.format(trunc(angulo)))
print('O Seno de {}° é {:.2f}'.format(trunc(angulo), sin(radians(angulo))))
print('O Cosseno de {}° é {:.2f}'.format(trunc(angulo), cos(radians(angulo))))
print('A Tangente de {}° é {:.2f}'.format(trunc(angulo), tan(radians(angulo))))
print('=' * 32)
