"""

print('Sistema de tabuada Impressionador')
numero = float(input('Digite o número que você quer calcular a tabuada: '))
for x in range(11):
    print('{} x {} = {}'.format(numero, x, numero * x)) """
    
print('Cálculos Impressionadores')
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura * largura
quant_necessaria = area / 2
print('Para uma area de {} m2'.format(area))
print('Precisa-se de {} litros de tinta'.format(quant_necessaria))