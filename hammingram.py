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



"""
def convertir1( binari ):
    if binari == 1 or binari == 0:

        decimal = 0
        for digit in binari:
            decimal = decimal * 2 + int(digit)
        return decimal

"""

nombre = "0100100100101000110101010010100000101101101110"
print(convertir2(nombre,3))
print(convertir2(nombre,4))
print(convertir2(nombre,5))




#print(convertir1(nombre))
