def llenarlista(): 
    listaA=[]
    m=int(input("Digite un numero"))
    if m>0 and m<11:
        print(m)
        listaA.append(m)
        pregunta=input("desea continuar?")
        while pregunta=="si":
             m=int(input("digite otro numero"))
             if m>0 and m<11:
                    listaA.append(m)
                    pregunta=input("Desea continuar?")
                    print(listaA)
        return(listaA)
    else:
        print("Digite un numero entre 11 y 0")
    
                                    
x=str(input("Que funcion desea operar?"))
lista=[1,2,3,4,5,6,7,8,9,10]

if x=="Interseccion":
    y=int(input("Cuantos grupos quiere crear"))
    if y==2:
        lista1=llenarlista()
        lista2=llenarlista()
        l=[lista1,lista2]
        c=set(1[0]).intersection(*1)
    elif y==3:
        lista1=llenarlista()
        lista2=llenarlista()
        lista3=llenarlista()
        l=[lista1,lista2,lista3]
        c=set(1[0]).intersection(*l)
        print(c)
    else:
        print("Por favor digite cuantos grupos desea crear")
        

        
    
                    
                           


    
        
