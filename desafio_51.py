# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão desta mesma PA: '))
d = n + (10 - 1) * r  # Este é o cálculo para o enésimo termo de uma PA, que, no caso,
# já está com o valor do termo que queremos encontrar substituido na equação
# Termo substituído -> (n - 1)

for i in range(n, d + r, r):  # laço i no intervalo(n, d + r, r)
    print(i, end=' -> ')  # Mostra na tela os valores que a PA assumirá
print('Acabou!')
