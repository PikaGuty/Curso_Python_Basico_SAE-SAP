b=True
while b:
    nom=input("Ingrese el nombre del estudiante  ")
    x=nom.upper()
    z=x[0]
    y=ord(z)
    sexo=input("Ingrese el sexo del estudiante  H/M")
    s=sexo.upper()
    if s=="H":
        if y>64 and y<77:
            print("Pertenece al grupo B")
            b=False
        elif y>76 and y<91:
            print("Pertenece al grupo A")
            b=False
        else:
            print("Debe ingresar un nombre correcto")
    elif s=="M":
        if y>64 and y<77:
            print("Pertenece al grupo A")
            b=False
        elif y>76 and y<91:
            print("Pertenece al grupo B")
            b=False
        else:
            print("Debe ingresar un nombre correcto")
    else:
        print("Debe ingresar un sexo correcto")
        
    
