import numpy as np
from matplotlib import pyplot as grafico
print("CONSIDERAREMOS PARA EL CALCULO DE LAS ESTADISTICAS DE RECEPCION, LAS SIGUIENTES CATEGORIAS DE RECEPCION")
print()
print()
print("Numero 1")
print("Recepción doble negativa: el saque que hace punto directo, porque cae al suelo sin que nadie lo toque, o porque provoca un error en la recepción.")
print()
print("Numero 2")
print("Recepción barra: la recepción no permite construir el ataque y por tanto entrega un free al equipo que saca.")
print()
print("Numero 3")
print("Recepción negativa: la recepción no permite jugar ataques de primer tiempo y solo se puede jugar pelota alta en la banda.")
print()
print("Numero 4")
print("Recepción exclamación: la recepción no debería poder jugar ataques de primer tiempo pero si pelota rápida en la banda.")
print()
print("Numero 5")
print("Recepción positiva: el equipo receptor puede jugar todas las posibilidades de ataque, pero la pelota está separada de la red (+-1,5 metros) o se aleja de la zona central del campo hacia las antenas.")
print()
print("Numero 6")
print("Recepción doble positiva: la recepción permite jugar todas las posibilidades de ataque con total comodidad para el colocador en la zona central del campo.")

print()
print()
print("A continuacion se le pedira el NUMERO DE LA CAMISETA y el ROL DEL JUGADOR")
print()
print("Cuando esten todos los jugadores escriba jugador=0")
print()
jugadores=dict()
diccionario=dict()
cant_pases=dict()
diccionario_1=dict()
diccionario_2=dict()
diccionario_3=dict()
diccionario_4=dict()
diccionario_5=dict()
diccionario_6=dict()
diccionario_grafico=dict()
lista_colores_lineas=['b-','g--','r-.','c-','m-','y-','k-','b--','g--','r--','c--','m--','y--','k--','b:','g:','r:','c:','m:','y:','k:','b-.','g-.','r-.','c-.','m-.','y-.','k-.']
lista=[]
jugador=""
numero=""

numero10=input("Ingrese el numero del jugador: ")

jugador=input("Ingrese el rol del jugador: ")

print()


while jugador!="0":
    try:
        numero = int(numero10)
        jugadores.update({numero: jugador})
        diccionario.update({numero: 0})
        cant_pases.update({numero:0})
        diccionario_1.update({numero:0})
        diccionario_2.update({numero:0})
        diccionario_3.update({numero:0})
        diccionario_4.update({numero:0})
        diccionario_5.update({numero:0})
        diccionario_6.update({numero:0})
        diccionario_grafico.update({numero:[]})
        lista.append(numero)
        numero10=input("Ingrese el numero del jugador: ")
        jugador=input("Ingrese el rol del jugador: ")
        print()
    except Exception:
        numero10 = input("Ingrese el numero del jugador: ")
        jugador = input("Ingrese el rol del jugador: ")
        print()
    
print()
print("Cuando se termine el set debera escribir Set= Fin")
print()
print("Si piden tiempo escriba Set=Tiempo para ver las estadisticas hasta el momento")
print()
print("Si ingresa un nuevo jugador escribir Set=Nuevo")
print()
suma=0
total=0
Set=0
suma_pase=0
ultimo_diccionario=dict()
sumatoria=0
pase1=0
numero_2=0
variable_rara=-100000000000000

while Set!="Fin":
    pase=input("Tipo de recepcion: ")
    numero_3=input("Que jugador recibio: ")
    try:
        pase1 = int(pase)
        numero_2 = int(numero_3)
        for C in diccionario.items():
            P,N=C
            if numero_2==P:
                if pase1<=6 and pase1>=1:
                    if pase1==6:
                        sumatoria+=1
                        diccionario_6[numero_2]+=1
                        
                    elif pase1==5:
                        diccionario_5[numero_2]+=1
                        
                    elif pase1==4:
                        diccionario_4[numero_2]+=1
                        
                    elif pase1==3:
                        diccionario_3[numero_2]+=1
                       
                    elif pase1==2:
                        diccionario_2[numero_2]+=1
                        
                    elif pase1==1:
                        diccionario_1[numero_2]+=1
                    
                    diccionario[numero_2]+=pase1
                    cant_pases[numero_2]+=6
                    #aqui e quede intentando hacer una lista dentro de un diccionario
                    diccionario_grafico[numero_2]+=str(pase1)
                    
    except Exception:
        1    
    Set=input("Set=")
    jugador=1
    if Set=="Nuevo":
        while jugador!="0":
            numero10=input("Ingrese el numero del jugador: ")

            jugador=input("Ingrese el rol del jugador: ")

            print()
            try:
                numero = int(numero10)
                jugadores.update({numero: jugador})
                diccionario.update({numero: 0})
                cant_pases.update({numero:0})
                diccionario_1.update({numero:0})
                diccionario_2.update({numero:0})
                diccionario_3.update({numero:0})
                diccionario_4.update({numero:0})
                diccionario_5.update({numero:0})
                diccionario_6.update({numero:0})
                diccionario_grafico.update({numero:[]})
                lista.append(numero)
                numero10=input("Ingrese el numero del jugador: ")
                jugador=input("Ingrese el rol del jugador: ")
                print()
            except Exception:
                numero10 = input("Ingrese el numero del jugador: ")
                jugador = input("Ingrese el rol del jugador: ")
                print()
    if Set=="Tiempo":
        for A in diccionario.items():
            num,sum_pases=A
            suma_de_pases=sum_pases*100
            for B in cant_pases.items():
                num2,total_pase=B
                if total_pase!=0 and num==num2:
                    porcentaje=suma_de_pases/total_pase
                    porcentaje=round(porcentaje,2)
                    ultimo_diccionario.update({num: porcentaje})

        lista_2=[]
        minimo=-1
        lista_3=[]
        lista_4=[]
        maximo=1000000000000000000000000000000000000000000000000000000000000000000000

        h=0
        j=0
        for C in ultimo_diccionario.items():
            num_c,porcentaje_c=C
            lista_2.append("El jugador numero "+str(num_c)+" tiene una efectividad de recepcion del "+str(porcentaje_c)+"%")
            if porcentaje_c>minimo:
                minimo=porcentaje_c
                j=num_c
                lista_3="La mejor recepcion es del numero "+str(num_c)+" con una efectividad del "+str(porcentaje_c)+"%"
            elif porcentaje==minimo:
                lista_3="La mejor recepcion es del numero "+str(num_c)+" y del numero "+str(j)+ " con una efectividad del "+str(porcentaje_c)+"%"
            if porcentaje_c<maximo:
                maximo=porcentaje_c
                h=num_c
                lista_4="La recepcion mas debil es del numero "+str(num_c)+" con una efectividad del "+str(porcentaje_c)+"%"
            elif porcentaje_c==maximo:
                lista_4="La recepcion mas debil es del numero "+str(num_c)+" y del numero "+str(h)+" con una efectividad del "+str(porcentaje_c)+"%"
            
        print()
        print(lista_3)
        print()
        print(lista_4)
        print()
        print(str(sumatoria)+ " recepciones doble positivo")
        print()
        print("Si necesita los datos especificos de algun jugador escriba Datos=Si ")
        print()
        pregunta_dato=input("Datos=")
        print()
        dato_jugador=""
        if pregunta_dato=="Si":
            while dato_jugador!="Listo":
                print()
                print("Una vez que ve termine de ver los datos escriba Listo ")
                print()
                dato_jugador=input("Ingrese el numero del jugador: ")
                print()
            
                try:
                    numero_jug=int(dato_jugador)
                    for H in diccionario.items():
                        h1,h2=H
                        if h1==numero_jug:
                            suma_rara=0
                            if diccionario_1[numero_jug]!=0:
                                print(str(diccionario_1[numero_jug])+" Recepcion(es) DOBLE NEGATIVO")
                                suma_rara+=diccionario_1[numero_jug]
                            if diccionario_2[numero_jug]!=0:
                                print(str(diccionario_2[numero_jug])+" Recepcion(es) BARRA")
                                suma_rara+=diccionario_2[numero_jug]
                            if diccionario_3[numero_jug]!=0:
                                print(str(diccionario_3[numero_jug])+" Recepcion(es) NEGATIVA(S)")
                                suma_rara+=diccionario_3[numero_jug]
                            if diccionario_4[numero_jug]!=0:
                                print(str(diccionario_4[numero_jug])+" Recepcion(es) EXCLAMACION")
                                suma_rara+=diccionario_4[numero_jug]
                            if diccionario_5[numero_jug]!=0:
                                print(str(diccionario_5[numero_jug])+" Recepcion(es) POSITIVA(S)")
                                suma_rara+=diccionario_5[numero_jug]
                            if diccionario_6[numero_jug]!=0:
                                print(str(diccionario_6[numero_jug])+" Recepcion(es) DOBLE POSITIVO")
                                suma_rara+=diccionario_6[numero_jug]
                            if suma_rara>=variable_rara:
                                variable_rara=suma_rara#cantidad maxima de pases para el grafico
                except Exception:
                    1

        print()
        print("Si desea ver el grafico de los jugadores escriba Grafico=Si")
        print()
        

        grafi=input("Grafico=")
        print()
        if grafi=="Si":
            for H in diccionario.items():
                h1,h2=H
                suma_rara=0
                if diccionario_1[h1]!=0:
                    
                    suma_rara+=diccionario_1[h1]
                if diccionario_2[h1]!=0:
                    
                    suma_rara+=diccionario_2[h1]
                if diccionario_3[h1]!=0:
                    
                    suma_rara+=diccionario_3[h1]
                if diccionario_4[h1]!=0:

                    suma_rara+=diccionario_4[h1]
                if diccionario_5[h1]!=0:
                    
                    suma_rara+=diccionario_5[h1]
                if diccionario_6[h1]!=0:
                    
                    suma_rara+=diccionario_6[h1]
                if suma_rara>=variable_rara:
                    variable_rara=suma_rara#cantidad maxima de pases para el grafico
            lista_x=np.arange(variable_rara)
            grafico.xticks(lista_x,(range(1,variable_rara+1)))
            suma_loca=0
            lista_lista_lista=[]
            b=[]
            for PA in jugadores.items():
                jug,pos=PA
                if diccionario_grafico[jug]!=[]:
                    lista_lista=[]
                
                    b=[int(x) for x in diccionario_grafico[jug]]
                    lista_lista=np.arange(1,len(diccionario_grafico)+1)
                    grafico.plot(b,lista_colores_lineas[suma_loca])
                    lista_lista_lista.append(jug)
                    
                    #aqui quedeeeeeeeeeeeee
                    suma_loca+=1
            grafico.xlabel("Cantidad de recepcion")
            grafico.ylabel("Tipo de recepcion")
            grafico.title("Grafico De Recepcion")
            grafico.legend(lista_lista)        
            grafico.show()

for A in diccionario.items():
    num,sum_pases=A
    suma_de_pases=sum_pases*100
    for B in cant_pases.items():
        num2,total_pase=B
        if total_pase!=0 and num==num2:
            porcentaje=suma_de_pases/total_pase
            porcentaje=round(porcentaje,2)
            ultimo_diccionario.update({num: porcentaje})

lista_5=[]
minimo=-1
lista_6=[]
lista_7=[]
maximo=1000000000000000000000000000000000000000000000000000000000000000000000

h=0
j=0
for C in ultimo_diccionario.items():
    num_c,porcentaje_c=C
    lista_5.append("El jugador numero "+str(num_c)+" tiene una efectividad de pase del "+str(porcentaje_c)+"%")
    if porcentaje_c>minimo:
        minimo=porcentaje_c
        j=num_c
        lista_6="La mejor recepcion es del numero "+str(num_c)+" con una efectividad del "+str(porcentaje_c)+"%"
    elif porcentaje==minimo:
        lista_6="La mejor recepcion es del numero "+str(num_c)+" y del numero "+str(j)+ " con una efectividad del "+str(porcentaje_c)+"%"
    if porcentaje_c<maximo:
        maximo=porcentaje_c
        h=num_c
        lista_7="La recepcion mas debil es del numero "+str(num_c)+" con una efectividad del "+str(porcentaje_c)+"%"
    elif porcentaje_c==maximo:
        lista_7="La recepcion mas debil es del numero "+str(num_c)+" y del numero "+str(h)+" con una efectividad del "+str(porcentaje_c)+"%"
    
print()
print(lista_6)
print()
print(lista_7)
print()
print(str(sumatoria)+ " recepcion doble positivo")
lista_datos=[]

print()
print("Si necesita los datos especificos de algun jugador escriba Datos=Si ")
print()
pregunta_dato=input("Datos=")
print()
dato_jugador=""
        
if pregunta_dato=="Si":
    while dato_jugador!="Listo":
        print()
        print("Una vez que ve termine de ver los datos escriba Listo ")
        print()
        dato_jugador=input("Ingrese el numero del jugador: ")
        print()

        try:
            numero_jug=int(dato_jugador)
            for W in diccionario.items():
                w1,w2=W
                if w1==numero_jug:
                    if diccionario_1[numero_jug]!=0:
                        print(str(diccionario_1[numero_jug])+" Recepcion(es) DOBLE NEGATIVO")
                    if diccionario_2[numero_jug]!=0:
                        print(str(diccionario_2[numero_jug])+" Recepcion(es) BARRA")
                    if diccionario_3[numero_jug]!=0:
                        print(str(diccionario_3[numero_jug])+" Recepcion(es) NEGATIVA(S)")
                    if diccionario_4[numero_jug]!=0:
                        print(str(diccionario_4[numero_jug])+" Recepcion(es) EXCLAMACION")
                    if diccionario_5[numero_jug]!=0:
                        print(str(diccionario_5[numero_jug])+" Recepcion(es) POSITIVA(S)")
                    if diccionario_6[numero_jug]!=0:
                        print(str(diccionario_6[numero_jug])+" Recepcion(es) DOBLE POSITIVO")
        except Exception:
                    1

print()
print("Si desea ver el grafico de los jugadores escriba Grafico=Si")
print()
        

grafi=input("Grafico=")
print()
if grafi=="Si":
    for H in diccionario.items():
        h1,h2=H
        suma_rara=0
        if diccionario_1[h1]!=0:
                    
            suma_rara+=diccionario_1[h1]
        if diccionario_2[h1]!=0:
                    
            suma_rara+=diccionario_2[h1]
        if diccionario_3[h1]!=0:
                    
            suma_rara+=diccionario_3[h1]
        if diccionario_4[h1]!=0:

            suma_rara+=diccionario_4[h1]
        if diccionario_5[h1]!=0:
                    
            suma_rara+=diccionario_5[h1]
        if diccionario_6[h1]!=0:
                    
            suma_rara+=diccionario_6[h1]
        if suma_rara>=variable_rara:
            variable_rara=suma_rara#cantidad maxima de pases para el grafico
    lista_x=np.arange(variable_rara)
    grafico.xticks(lista_x,(range(1,variable_rara+1)))
    suma_loca=0
    lista_lista_lista=[]
    b=[]
    for PA in jugadores.items():
        jug,pos=PA
        if diccionario_grafico[jug]!=[]:
            lista_lista=[]
                    
            b=[int(x) for x in diccionario_grafico[jug]]
            lista_lista=np.arange(1,len(diccionario_grafico)+1)
            grafico.plot(b,lista_colores_lineas[suma_loca])
            lista_lista_lista.append(jug)
                    
            #aqui quedeeeeeeeeeeeee
            suma_loca+=1
    grafico.xlabel("Cantidad de recepcion")
    grafico.ylabel("Tipo de recepcion")
    grafico.title("Grafico De Recepcion")
    grafico.legend(lista_lista)        
    grafico.show()
print()
print("GRACIAS POR USAR EL CODIGO DE CHARLIE")
        

