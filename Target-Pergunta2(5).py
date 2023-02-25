# Solicitando entrada do usuário e fazendo uma cópia; 
entrada = input('Digite uma frase que você queira inverter: ')
entrada_copia = entrada
resposta = []

# Código responsável por inserir os caracteres invertidos em uma lista;

for char in entrada:
    resposta.append(entrada_copia[-1])
    entrada_copia = entrada_copia[:-1] 

# Função que transforma lista em string;

resposta = ''.join(resposta)

print(f'FRASE: "{entrada}"\nFrase invertida: {resposta}')