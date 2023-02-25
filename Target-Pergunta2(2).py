fibonacci = [0, 1]

entrada = int(input('Insira um número para saber se ele pertence a sequência Fibonacci: '))

# Calculando a seqûencia Fibonacci até o valor de entrada do usuário;
 
while fibonacci[-1] < entrada:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)

# Verificando se a entrada do usuário pertence a seqûencia Fibonacci;  
if entrada in fibonacci:
    print(f'{entrada} pertence a sequência Fibonacci, sendo o {fibonacci.index(entrada) + 1}° número da seqûencia.')
else:
    print(f'{entrada} não é um número fibonacci.')