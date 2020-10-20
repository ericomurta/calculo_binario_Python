# funcoes utilizadas
def soma_binario(a, b):
    convert_a=int(a,2)
    convert_b=int(b,2)
    soma_dec = convert_a + convert_b
    soma_bin = "%08d" % int(bin(soma_dec)[2:])
    return soma_bin

def subtracao_binario(a,b):
    convert_a=int(a, 2)
    convert_b=int(b, 2)
    sub_dec = (convert_a) - (convert_b)
    sub_bin = "%08d" % int(bin(sub_dec)[2:])
    return sub_bin

def multiplicacao_binario(a,b):
    convert_a=int(a, 2)
    convert_b=int(b, 2)
    mult_dec = (convert_a)*(convert_b)
    mult_bin = "%08d" % int(bin(mult_dec)[2:])
    return mult_bin

def divisao_binario(a,b):
    convert_a=int(a, 2)
    convert_b=int(b, 2)
    div_dec = convert_a//convert_b
    div_bin = "%08d" % int(bin(div_dec)[2:])
    return div_bin

def resto_binario(a,b):
    convert_a=int(a, 2)
    convert_b=int(b, 2)
    resto_dec = convert_a % convert_b
    resto_bin = "%08d" % int(bin(resto_dec)[2:])
    return resto_bin
#fim funcao


# inicio
pergunta = input('Digite um dos sinais para iniciar a operação: +, -, * , /, %')

# bloco soma
if pergunta == '+' :
    pergunta1 = input('Digite o primeiro número entre 0 e 255 em binário.')
    if pergunta1 < '11111111' and pergunta1 > '00000000':
        numero1 = pergunta1
        pergunta2 = input('Digite o segundo número entre 0 e 255 em binário.')
        if pergunta2 < '11111111' and pergunta2 > '00000000':
            numero2 = pergunta2
            print(soma_binario(numero1, numero2))
        else:
            print('O número informado não está dentro do intervalo citado')
    else:
        print('O número informado não está dentro do intervalo citado.')

# bloco subtracao
elif pergunta == '-' :
    pergunta1 = input('Digite o primeiro número entre 0 e 255 em binário.')
    if pergunta1 < '11111111' and pergunta1 > '00000000':
        numero1 = pergunta1
        pergunta2 = input('Digite o segundo número entre 0 e 255 em binário.')
        if pergunta2 < '11111111' and pergunta2 > '00000000':
            numero2 = pergunta2
            print(subtracao_binario(numero1, numero2))
        else:
            print('O número informado não está dentro do intervalo citado.')
    else:
        print('O número informado não está dentro do intervalo citado.')

# bloco multiplicacao
elif pergunta == '*' :
    pergunta1 = input('Digite o primeiro número entre 0 e 255 em binário.')
    if pergunta1 < '11111111' and pergunta1 > '00000000':
        numero1 = pergunta1
        pergunta2 = input('Digite o segundo número entre 0 e 255 em binário.')
        if pergunta2 < '11111111' and pergunta2 > '00000000':
            numero2 = pergunta2
            print(multiplicacao_binario(numero1, numero2))
        else:
            print('O número informado não está dentro do intervalo citado.')
    else:
        print('O número informado não está dentro do intervalo citado.')

# bloco divisao
elif pergunta == '/' :
    pergunta1 = input('Digite o primeiro número entre 0 e 255 em binário.')
    if pergunta1 < '11111111' and pergunta1 > '00000000':
        numero1 = pergunta1
        pergunta2 = input('Digite o segundo número entre 0 e 255 em binário.')
        if pergunta2 < '11111111' and pergunta2 > '00000000':
            numero2 = pergunta2
            print(divisao_binario(numero1, numero2))
        else:
            print('O número informado não está dentro do intervalo citado.')
    else:
        print('O número informado não está dentro do intervalo citado.')

# bloco resto divisao
elif pergunta == '%' :
    pergunta1 = input('Digite o primeiro número entre 0 e 255 em binário.')
    if pergunta1 < '11111111' and pergunta1 > '00000000':
        numero1 = pergunta1
        pergunta2 = input('Digite o segundo número entre 0 e 255 em binário.')
        if pergunta2 < '11111111' and pergunta2 > '00000000':
            numero2 = pergunta2
            print(resto_binario(numero1, numero2))
        else:
            print('O número informado não está dentro do intervalo citado.')
    else:
        print('O número informado não está dentro do intervalo citado.')

else:
    print('Operador inválido')