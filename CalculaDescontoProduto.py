# Programa calcula o desconto do produto a prazo e á vista
# Para pagamento á vista desconto é de 10% para pagamento parcelado, desconto de 5%

preco = float(input('Digite o preço do produto: R$ '))
tipoPagamento = int(input('Escolha a forma de pagamento: digite 1 á vista ou 2 parcelar:'))

if(tipoPagamento == 1):
    precoDesconto = preco - (preco * 5 / 100)
    print('O preço do produto com 5% é de: R${:.2f}'.format(precoDesconto))
else:
    precoDesconto = preco - (preco * 10 / 100)
    print('O preço do produto com 10% é de: R${:.2f}'.format(precoDesconto))


