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

nombre = "10110100100100101000110101010010100000101101101110"

lista = convertir2(nombre,4)

print( hamming4( lista ) )




#print(convertir1(nombre))
