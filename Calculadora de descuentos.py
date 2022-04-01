precioTotal=0 

precio=float(input("Ingrese precio del producto:"))
cantidad=int(input("Ingrese cantidad:"))
promocion=input("Ingrese una opción:\n \n A (S/D)          B (80%)          C (70%)\n\n D (60%)          E (50%)          F (30%)\n\n G (10%)          X(2X1)           T(3X2)\n")

while precio!=0:
    if promocion.lower()=="a" or promocion.lower()=="b" or promocion.lower()=="c" or promocion.lower()=="d" or promocion.lower()=="e"or promocion.lower()=="x" or promocion.lower()=="t": 
        if cantidad==1:
            precioP=precio
            print("Precio Producto: ", precioP)
        elif cantidad>1:
            if promocion.lower()=="a":
                precioP=precio*cantidad
                print("Precio Productos: ", precioP)
            elif cantidad%2==0:
                if promocion.lower()=="b":
                    precioP=(cantidad/2)*precio*1.2
                    print("Precio Productos:",precioP)
              
                elif promocion.lower()=="c":       
                    precioP=(cantidad/2)*precio*1.3
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="d":
                    precioP=(cantidad/2)*precio*1.4
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="e": 
                    precioP=(cantidad/2)*precio*1.5
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="x":
                    precioP=(precio*cantidad)/2
                    print("Precio Productos:",precioP) 
                elif promocion.lower()=="t":
                    cant=cantidad/3
                    if cantidad%3==0:
                        precioP=(cantidad-cant)*precio
                        print("Precio Productos:",precioP)
                    elif cantidad%3==1:
                        precioP=((cantidad-cant)*precio)
                        print("Precio Productos:",precioP)
                    elif cantidad%3==2:
                        precioP=((cantidad-cant)*(precio*2))
                        print("Precio Productos:",precioP)    
                    
                    
            elif cantidad%2==1:
                if promocion.lower()=="b":
                    precioP=((cantidad-1)/2*precio*1.2+precio)
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="c":
                    precioP=((cantidad-1)/2*precio*1.3+precio)
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="d":
                    precioP=((cantidad-1)/2*precio*1.4+precio)
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="e":
                    precioP=((cantidad-1)/2*precio*1.5+precio)
                    print("Precio Productos:",precioP)
                elif promocion.lower()=="x":
                    precioP=precio*(cantidad-1)/2+precio
                    print("Precio Productos:",precioP)            
    elif promocion.lower()=="f" and cantidad>=1:
        precioP=(precio*cantidad)-(precio*cantidad*0.3)
        print("Precio Productos",precioP)  
    elif promocion.lower()=="g" and cantidad>=1:
        precioP=(precio*cantidad)-(precio*cantidad*0.1)
        print("Precio Productos",precioP)       
     

    precioTotal=precioTotal+precioP
    precio=float(input("Ingrese precio del producto:"))
    cantidad=int(input("Ingrese cantidad:"))
    promocion=input("Ingrese una opción:\n \n A (S/D)          B (80%)          C (70%)\n\n D (60%)          E (50%)          F (30%)\n\n G (10%)          X(2X1)           T(3X2)\n")
print("Precio Total:",precioTotal)
x=input()
