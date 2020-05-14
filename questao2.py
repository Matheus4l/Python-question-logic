# Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, },
# [ ou ].
# Dois brackets são considerados um par combinado se o bracket de
# abertura (isto é, (, [ou {) ocorre à esquerda de um bracket de fechamento
# (ou seja,),] ou} do mesmo tipo exato. Existem três tipos de pares de
# brackets : [ ], { } e ( ).
# Um par de brackets correspondente não é balanceado se o de abertura e
# o de fechamento não corresponderem entre si. Por exemplo, { [ ( ] ) } não
# é balanceado porque o conteúdo entre {e} não é balanceado. O primeiro
# bracket inclui o de abertura, (, e o segundo inclui um bracket de
# fechamento desbalanceado,].
# EXEMPLO
# {[()]} SIM
# {[(])} NAO
# {{[[(())]]}} SIM
# Dado sequencias de caracteres, determine se cada sequência de brackets
# é balanceada. Se uma string estiver balanceada, retorne SIM. Caso
# contrário, retorne NAO.

bracket = input("Insira  obracket:")

numRepeticoes = len(bracket)/2 # dividindo a lista pela metade 

def inverBracket(data):
    if data =="{":
        return "}"
    elif data == "[":
        return "]"
    elif data == "(":
        return ")"
    else:
        return "Bracket invalido"

x=-1# serve pra começar a lista do final 
resposta = "sim"

for i in range(int(numRepeticoes)):# a ideia e verificar ponta a ponta 
    ultimoElemento = x
    bracketIverse  = inverBracket(bracket[i]) # chamndo a função pra busca o caracter oposto 

    if bracket[x] != bracketIverse:
       resposta = "não"
       break
    x=x-1             #aqui eu faço a lista de tras pra frente 

print("\n",bracket,"=",resposta)



