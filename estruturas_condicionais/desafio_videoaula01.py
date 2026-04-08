#criar um mini sistema de comprar pão

#variavel que define o preço do pão
preco_pao = 4.0
pagamento_cliente = float(input("Digite o valor pago na compra: "))

if preco_pao <= pagamento_cliente:
    print("Pagamento bem sucedido! Espere a emissão da nota fiscal.")
else:
    print("Dinheiro insuficiente.")