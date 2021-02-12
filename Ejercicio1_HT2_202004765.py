y="CONTRASEÑA"
b=True
c=1
while b:
    x=input("Ingrese la contraseña  ")
    z=x.upper()
    if z==y:
        print("***************************************")
        print("* La contraseña ingresada es correcta *")
        print("***************************************")
        b=False
    else:
        print("*******************************")
        print("* La contraseña es incorrecta *")
        print("*******************************")
        c=c+1
        if c==3:
            print("********************************")
            print("* Tiene una última oportunidad *")
            print("********************************")
        elif c>3:
            print("************************************************")
            print("* Ha excedido el límite de intentos permitidos *")
            print("************************************************")
            b=False
