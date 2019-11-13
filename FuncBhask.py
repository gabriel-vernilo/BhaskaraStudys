#live ♥

#Bhaskara

Values = input('type the a, b, and c values\n').split()
a = float(Values[0])
b = float(Values[1])
c = float(Values[2])

def Delta(a,b,c):
    delta = ((b**2) - (4*a*c))
    Bhaskara(a,b,delta)


def Bhaskara(a,b,delta):
    x1 = ((b*-1) + (delta**(1/2)))/(2*a)
    x2 = ((b*-1) - (delta**(1/2)))/(2*a)
    print(f'R: {x1} ; {x2} ')

Delta(a,b,c)