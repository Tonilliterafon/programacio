def canvia (numero,posicio):
    #print( "corregim " + numero + "  a posicio: " + str(posicio) )
    numero = list( numero )
    numero[posicio] = str( 1 - int( numero[posicio] ) )
    return ''.join(numero)
    
def corregir(paquet):
    #hem de troabr cada posició
    p = str(paquet)
    #miram paritats correctes
    F1 = (int(p[0]) + int(p[2]) + int(p[4]) + int(p[6]))%2
    F2 = (int(p[1]) + int(p[2]) + int(p[5]) + int(p[6]))%2
    F3 = (int(p[3]) + int(p[4]) + int(p[5]) + int(p[6]))%2
    print ("f1: ", F1)
    print ("f2: ", F2)
    print ("f3: ", F3)
 
    #error_bit = (F3 * 4 + F2 * 2 + F1)-1
    
    if F1 and not(F2) and not(F3):
        paquet = canvia(paquet,0)
    if not(F1) and F2 and not(F3):
        paquet = canvia(paquet,1)
    if not(F1) and not(F2) and F3:
        paquet = canvia(paquet,3)
    if F1 and F2 and not(F3):
        paquet = canvia(paquet,2)
    if F1 and not(F2) and F3:
        paquet = canvia(paquet,4)
    if not(F1) and F2 and F3:
        paquet = canvia(paquet,5)
    if F1 and F2 and F3:
        paquet = canvia(paquet,6)
    
    # Identificar el bit erróneo
    

    return paquet   
 
 
 
def convertir2 (nombre,qbits):
    #ha de retornar l'str binari a deicmal
    #binari tallat en qbits
    llista = []
    a = 0
    b = qbits
 
    for x in range (int(len(nombre)/qbits)):
        llista.append(nombre[a:b])
        a += qbits
        b += qbits
 
    #print(nombre[a:b])
    #print(nombre[4:7])
    #print(nombre[8:11])
    return llista
 
def hamming4 ( lista ):
    codificado = []
    for paquete in lista:
        # Obtenemos bits de datos
        P1 = int(paquete[0]) + int(paquete[1]) + int(paquete[3])
        P2 = int(paquete[0]) + int(paquete[2]) + int(paquete[3])
        P3 = int(paquete[1]) + int(paquete[2]) + int(paquete[3])
     
        # Calculamos paridad
        if ( P1 % 2 != 0 ): 
            P1 = 1
        else:
            P1 = 0
        
        if ( P2 % 2 != 0 ):
            P2 = 1
        else:
            P2 = 0
        
        if ( P3 % 2 != 0 ):
            P3 = 1
        else:
            P3 = 0
        codificado.append( str(P1) + str(P2) + paquete[0] + str(P3) + paquete[1] + paquete[2] + paquete[3] )
    
    return codificado
 
"""
def convertir1( binari ):
    if binari == 1 or binari == 0:
        decimal = 0
        for digit in binari:
            decimal = decimal * 2 + int(digit)
        return decimal
"""
 
#nombre = "10110100100100101000110101010010100000101101101110"
"""nombre = "0111101111000101"
 
 
qbits = int(input("Insereix la divisó de bits: "))
 
lista = convertir2(nombre,qbits)
 
print( hamming4( lista ) )  
 
"""
print("Rebut:   0100011")
print("Calculat:"+corregir("0110011"))
