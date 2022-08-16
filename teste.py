print('Caso deseje parar o código aperte enter sem nenhum valor')
numero = input('Digite os números que você deseja calcular a média: ')
numeros = []
soma_num = 0

while numero != '':
    if numero == '':
        break
    numeros.append(float(numero))
    numero = input('Digite os números que você deseja calcular a média: ')
    
quant_num = len(numeros)
soma_num = sum(numeros)
media = soma_num / quant_num

print('A soma dos números é: {}'.format(soma_num))
print('Você digitou: {} valores.'.format(quant_num))
print('A média dos calculos é: {}'.format(media))

#for variaveis in var:
    