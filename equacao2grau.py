a = int(input("digite o valor de a (acompanha x^2)\n"))
b = int(input("digite o valor de b (acomoanha x)\n"))
c = int(input("digite o valor de c (não acompanha variável)\n"))
print(" ")
print("\033[1;93m" "RESPOSTAS :")
print('\033[1;97m' "-" * 10, )

def bhaskara(a, b, c):
    delta = (b**2 - 4*a*c)
    produto = c/a
    soma = (b * -1) /a

    if(delta>0):
        print("delta é maior que zero")
        if(produto>0):
            print("raizes reais e iguais")
            if(soma>0):
                print("e positivos")
            elif(soma< 0):
                print("e negativos")
            else:
                print("soma é igual a 0")
        elif(produto < 0):
            print("raizes reais e diferentes, sendo uma positiva e outra negativa")
        else:
            print("produto é igual a 0")
    elif(delta == 0 ):
        print("duas raizes reais e iguais (ou uma raiz apenas)")
    else:
        print("delta menor que 0, não há raizes reias")

    x1 = ((b * -1) + (delta**(1/2))) / (2*a)
    x2 = ((b* -1 ) - (delta**(1/2))) / (2*a)
    print("seu delta é {}".format(delta))
    print("seu x1 é {} , e seu x2 é {}".format(x1, x2))

resposta = bhaskara(a, b, c)