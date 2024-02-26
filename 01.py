print("holad")
def factorial(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b
hola= factorial(0)
print(hola)
print("aproximación de seno")
while True:
    def sen(a):
        c=0
        for i in range(31):
            c = c + (((a ** (2*i+1))/factorial(2*i+1)) * ((-1) ** i))
        return c
    print("Ingrese un número")
    s=float(input())
    se=sen(s)
    print(se)
    if s==0:
        break