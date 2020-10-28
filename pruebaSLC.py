def llenarlista(): 
    listaA=[]
    a=int(input('Cuantos numeros tiene el primer grupo'))
    z=int(input('Cuantos numeros tiene el segundo grupo'))
    w=int(input('Cuantos numeros tiene el tercer grupo'))
    i=1
    m=int(input("Digite un numero"))
    if a>0:
        if m>0 and m<11:
            print(m)
            listaA.append(m)
            while i<a:
                    m=int(input("digite otro numero"))
                    if m>0 and m<11:
                        listaA.append(m)
                    print(listaA)
                    i += 1
            return(listaA)
        else:
            print("Digite un numero del 1 al 10")
    else:
        print('la lista no puede tener menos de un numero')
x=str(input("Que funcion desea operar?"))
lista=[1,2,3,4,5,6,7,8,9,10]

if x=="Interseccion" or 'i':
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
        

        
    
                    
                           


    
        
