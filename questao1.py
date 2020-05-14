# Dado um array de números inteiros, retorne os
# índices dos dois números de forma que eles se
# somem a um alvo específico.
# Você pode assumir quecada entrada teria
# exatamente uma solução, e você não pode usar o
# mesmo elemento duas vezes.
import os
import random


clear = lambda: os.system('clear')

arrayNum = random.sample(range(50), 12)
sair = 1

while sair == 1:
    clear()

    print("Para acerta o alvo voce deve escolher um numero que é a some de 2 numeros na lista abaixo\n")
    print(arrayNum)
    inputValor = input('\n Alvo:')
    alvo  = int(inputValor)
    achou = 0

    for i in range(len(arrayNum)):
        
        for x in range(i+1,len(arrayNum)):
            
            soma = arrayNum[i]+arrayNum[x]
            
            if soma == alvo:
              print("----Resultado-----")
              print("Alvo atingido! posição:",i+1,"=",arrayNum[i],"e posição:",x+1,"=",arrayNum[x]," removidas\n")
              print("----Antigo----\n",arrayNum)
              

              arrayNum.remove(arrayNum[i])
              arrayNum.remove(arrayNum[x])
             
              achou = 1  
              print("\n----Novo----\n",arrayNum)
              break
           
        if achou == 1:
            break
    if achou == 0:
        print('Alvo Nao encontrado ')
    
    sair_input = input("\nSair [0]  continuar [1]: ")
    sair = int(sair_input)

else:
    clear()
    print("\nAté Mais!")

 

