
# Digamos que você tenha um array para o qual o
# elemento i é o preço de uma determinada ação no
# dia i.
# Se você tivesse permissão para concluir no máximo
# uma transação (ou seja, comprar uma e vender uma
# ação), crie um algoritmo para encontrar o lucro
# máximo.
# Note que você não pode vender uma ação antes
# de comprar.

day_trade= list() #array com os valores 
print('O day trade tem tem 5 dias!\n')
print('Coloque o valores para cada dia !')

#guardando os valor na lista 
for i in range(5):                        
    print("\nDia",i+1)
    n = input("Valor:")
    day_trade.append(int(n))


lucro=0
#Aqui vou analisar cada elemento fazendo a subtração  
for i in range(5):  
   for x in range(i+1,5): 
        # pego o possivel valor de compra e verifico o "i"=valor de compra com "x"=possivel valor de venda
        lucroEstimado = day_trade[x]- day_trade[i]
        
        if lucro < lucroEstimado:  #Quardo a informação do maior lucro  
            lucro     = lucroEstimado
            diaCompra =  day_trade.index(day_trade[i]) #retorna o index do valor "i"
            diaVenda  =  day_trade.index(day_trade[x]) #retorna o index do valor "x"
        
if lucro == 0:
    print("\n---------Resultado-----------\n")
    print("Não compre ações! Não existe lucro ")
    print(day_trade)

else:
    print("\n---------Resultado-----------\n")
    print('Dia da Compra:',diaCompra+1)# +1 e pra simular o dia já que a lista começa do 0 
    print('Dia da Venda:',diaVenda+1)  
    print("Seu lucro é de:",lucro)
    print(day_trade)


