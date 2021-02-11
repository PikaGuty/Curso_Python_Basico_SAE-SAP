x=int(input("Ingrese un numero entero  "))
c=1
y=0
while c<=x:
    r=x%c
    if r==0:
        y=y+1
    c=c+1
if y<=2:
    print("El número es primo")
else:
    print("El número es compuesto")