def retornar_meu_nome(nome, sobrenome):
    resultado = 'Olá, seu nome é: ' + nome + ' ' + sobrenome
    return resultado

# variavel = chamada de funcao(argumento 1, argumento 2)
nome_input = input('Digite seu nome: ')
sobrenome_input = input('Digite seu sobrenome: ')

meu_nome = retornar_meu_nome(sobrenome=sobrenome_input, nome=nome_input)
print(meu_nome)

def somar(a, b):
    resultado = a + b
    if(resultado > 40):
        return resultado
    else:
        return "Ops, só retorno valores acima de 40"

valor1 = float(input('digite o valor 1: '))
valor2 = float(input('digite o valor 2: '))
resultado = somar(valor1, valor2)
print(resultado)