# Criando funções para evitar repetição de código;

def porcentagem(valor, total):
    return ((valor/total) * 100)

def resposta(valor, estado ,total):
    print(f'\nOs R${valor:,.2f} de faturamento de {estado} equivale a {porcentagem(valor, total):.2f}% do valor total de faturamento.\n')

#Criando dataset de faturamento dos estados;

faturamento = [['SP', 'RJ', 'MG', 'ES', 'Outros' ],
 [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]]

# Calculando o faturamento total (soma dos valores);

total = 0
for valor in faturamento[1]:
    total+=valor

# Criação da interface; 
while True:
    try:
        entrada = int(input('De qual estado quer saber a % de faturamento?\n[1] SP\n[2] RJ\n[3] MG\n[4] ES\n[5] Outros\nDigite o número aqui: '))
        if entrada == 1:
            resposta(faturamento[1][entrada - 1],faturamento[0][entrada - 1], total)
        elif entrada == 2:
            resposta(faturamento[1][entrada - 1],faturamento[0][entrada - 1], total)
        elif entrada == 3:
            resposta(faturamento[1][entrada - 1],faturamento[0][entrada - 1], total)
        elif entrada == 4:
            resposta(faturamento[1][entrada - 1],faturamento[0][entrada - 1], total)
        elif entrada == 5:
            resposta(faturamento[1][entrada - 1],faturamento[0][entrada - 1], total)
        else:
            print('Erro, ensira um valor válido')        
    except:
        print('Erro, ensira um valor válido')

    verificar = input('Deseja verificar outro valor?\n[1] Sim\n[Outra tecla] Não\nDigite Aqui: ')
    if verificar == '1':
        pass
    else:
        break