
import string

x= "( - 9 )"
z= '( b ( < c ( v a ) ) )'
PROPOSICAO = ['0','1','2','3','4','5','6','7','8','9'],list(string.ascii_lowercase[0:26])
ABREPAREN= "("
FECHAPAREN= ")"
OPERATORUNARIO = '-'
OPERATORBINARIO = ['^','v' ,'<' ,'>']

teste = ['teste1.txt', 'teste2.txt' , 'teste3.txt']
for n in teste:
    with open(n) as f:
        for exemplo in f:
            lista = exemplo.split()

            estado = 1

            for i in range(0, len(lista)):
                #print(lista[i])
                if estado == 1 and lista[i] == ABREPAREN:
                    if lista[i + 1] in PROPOSICAO[0] or lista[i] in PROPOSICAO[1]:
                        estado = 4
                    elif lista[i + 1] == OPERATORUNARIO:
                        estado = 2
                    elif lista[i + 1] in OPERATORBINARIO:
                        estado = 3


                elif estado == 2 and lista[i] == OPERATORUNARIO:

                    estado = 4

                elif estado == 3 and lista[i] in OPERATORBINARIO:
                    estado = 4

                elif estado == 4 and lista[i] in PROPOSICAO[0] or lista[i] in PROPOSICAO[1]:
                    estado = 5
                    if lista[i + 1] == ABREPAREN:
                        estado = 1
                    elif lista[i + 1] == FECHAPAREN:
                        estado = 5

                elif estado == 5 and lista[i] == FECHAPAREN:
                    estado = 5
                    
                
                else:
                    print("invalido")
                    break

            if estado == 5:
                print("valido")


