# importando biblioteca Json;
import json

# Abrindo o json como fonte dos dados;

with open('dados.json', encoding = 'utf-8') as dados_json:
    dados = json.load(dados_json)

# Armazenando os faturamentos diários diferentes de 0 em uma lista;

valores_lista = [valor['valor'] for valor in dados if valor['valor'] != 0]

# Tirando a média da lista de faturamento;

media = sum(valores_lista) / len(valores_lista)

# Variáveis necessárias para responder as questões;

menor_valor = 100**20
menor_valor_dia = 0

maior_valor = 0
maior_valor_dia = 0

contador = 0

# Criação da interface;
while True: 
    entrada = input('''\nDigite o número referente a informação necessária:\n
[1] O menor valor de faturamento ocorrido em um dia do mês;
[2] O maior valor de faturamento ocorrido em um dia do mês;
[3] Número de dias no mês em que o valor de faturamento diário foi superior à média mensal;
Digite aqui: ''')

# Respondendo as questões solicitadas:

    if entrada == '1':
        for i in range(len(dados)):
            if dados[i]['valor'] < menor_valor and dados[i]['valor'] != 0:
                menor_valor = dados[i]['valor']
                menor_valor_dia = dados[i]['dia']
        print(f'\nO menor valor de faturamento foi {menor_valor}, que ocorreu no dia {menor_valor_dia}')

    if entrada == '2':
        for i in range(len(dados)):
            if dados[i]['valor'] > maior_valor:
                maior_valor = dados[i]['valor']
                maior_valor_dia = dados[i]['dia']
        print(f'\nO maior valor de faturamento foi {maior_valor}, que ocorreu no dia {maior_valor_dia}')

    if entrada == '3':
        for i in range(len(dados)):
            if dados[i]['valor'] > media:
                contador += 1
        print(f'\nDos {len(dados)} dias do mês, {contador} dias tiveram faturamento superior a média mensal ({media:.4f})')

    entrada = input('''\nDeseja acessar a interface novamente?:\n
[1] Sim;
[Outra tecla] Não;
Digite aqui: ''')

    if entrada != '1':
        break