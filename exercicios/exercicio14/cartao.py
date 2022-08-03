meuCartao = int(input("Digite o número do seu cartão de crédito, caso tenha esgotado os números de pesquisa, digite 0 para encerrar: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("Consta seu cartão na lista!")
else:
    print("Não consta seu cartão na lista!")