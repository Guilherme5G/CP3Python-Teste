def verifica_numero(msg):
    escolha = input(msg)
    while not escolha.isnumeric():
        escolha = input(msg)
    return int(escolha)

def forcar_opcao(lista, msg):
    opcoes = ", ".join(lista)
    print("\n--------------------")
    escolha = input(f"\n{msg}\n{opcoes}\n->")
    while escolha not in lista:
        escolha = input(f"\n{msg}\n{opcoes}\n->")
    return escolha

def maior_valor(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def menor_valor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

def media_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media


def achar_indice(lista, escolha):
    for i in range(len(lista)):
        if escolha == lista[i]:
            indice = i
            break
    return indice


print("Bbem vindo a nossa vinheria!!")
anoNascimento = verifica_numero("Qual seu ano de nascimento -> ")
idade = 2025 - anoNascimento

if idade < 18:
    print("Voce e menor de idade, nao pode inserir bebidas alcolica🙁")
    print("Encerrando programa. Tenha um otimo dia!")
else:
    vinhos = ['Dom Bosco', 'Goes', 'Pérgola', 'Cabernet Sauvignon']
    precos = [17, 15, 23, 70]
    quantidadeVinhos = [0] * len(vinhos)

    subtotal = 0

    endereco = input("Qual seu endereco para entrega? \n-> ")

    custoMedio = media_lista(precos)
    vinhoCaro = maior_valor(precos)
    vinhoBarato = menor_valor(precos)
    print(f"O custo medio dos vinhos da nossa vinheria e de {custoMedio},"
          f"sendo o mais caro: {vinhos[vinhoCaro]}, custando {precos[vinhoCaro]}, e o mais barato: {vinhos[vinhoBarato]}, custando {precos[vinhoBarato]}")

    while True:

        vinhoEscolhido = forcar_opcao(vinhos, "Qual vinho deseja comprar?\n")
        quantidadeEscolhida = verifica_numero("Quantas garrafas deseja comprar?\n-> ")
        indiceVinho = achar_indice(vinhos, vinhoEscolhido)
        quantidadeVinhos[indiceVinho] += quantidadeEscolhida

        encerrar = forcar_opcao(['Continuar', 'Encerrar'], "Deseja encerrar a compra?")
        if encerrar == 'Encerrar':
            break

    for i in range(len(vinhos)):
        subtotal += precos[i] * quantidadeVinhos[i]

    if subtotal > 500:
        frete = 0
        print("\nO seu pedido ultrapassou o valor de R$500,00 e voce ganhou FRETE GRATIS!")
    else:
        frete = subtotal * 0.10

    total = subtotal + frete
    print("\n-------------------------")
    print(f"Agradecemos a sua compra conosco! O seu pedido sera entregue no endereco: {endereco}.\n"
          
          f"\nQuantidade de cada garrafa: ")
    for i in range(len(vinhos)):
        print(f"{vinhos[i]} - {quantidadeVinhos[i]} garrafa(s)")

    print(f"\nO total do seu pedido e R${total:.2f}.")

