print('=' * 32, 'DESAFIO 15', '=' * 32)
km = float(input('Quantos kilômetros foram rodados? '))
km *= 0.15
da = int(input('Quantos dias você ficou com o carro? '))
da *= 60
t = km + da
print('Você terá que pagar R${:.2f} pelos km rodados e R${:.2f} pelos dias de uso.'.format(km, da))
print('Ao total você pagará R${:.2f} pelo aluguel do carro.'.format(t))
print('=' * 76)
