# Aquesta funció canvia un digit de una cadena
def canvia (numero,posicio):
    numero = list( numero )
    numero[posicio] = str( 1 - int( numero[posicio] ) )
    return ''.join(numero)

# Aquesta funció identifica el bit erroni i el corregeix si es necessari
def corregir(paquet):
    # hem de trobar cada posició
    p = str(paquet)
    # Miram paritats correctes
    F1 = (int(p[0]) + int(p[2]) + int(p[4]) + int(p[6]))%2
    F2 = (int(p[1]) + int(p[2]) + int(p[5]) + int(p[6]))%2
    F3 = (int(p[3]) + int(p[4]) + int(p[5]) + int(p[6]))%2

    # Miram els cassos possible de error i canviam bit
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

    return paquet   


# Aquesta funció converteix un string a llista de strings de qbits de longitud
def convertir2 (nombre,qbits):
    llista = []
    a = 0
    b = qbits
    
    for x in range (int(len(nombre)/qbits)):
        llista.append(nombre[a:b])
        a += qbits
        b += qbits

    return llista

# Aquesta funció codifica tots els paquets de una llista
def hamming4 ( lista ):
    codificado = []
    for paquete in lista:
        
        # Calculam bits de paritat
        P1 = int(paquete[0]) + int(paquete[1]) + int(paquete[3])
        P2 = int(paquete[0]) + int(paquete[2]) + int(paquete[3])
        P3 = int(paquete[1]) + int(paquete[2]) + int(paquete[3])

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
            
        # Afegim a la llista les dades + paridats calculades
        codificado.append( str(P1) + str(P2) + paquete[0] + str(P3) + paquete[1] + paquete[2] + paquete[3] )

    return codificado

# Aquesta funció decodifica i corregeix els paquets de la llista
def decodifica( lista ):
    decodificat = []
    for i in lista:
        paquet = corregir( i )
        decodificat.append( paquet )
    
    return decodificat


# INICI PROGRAMA

# Demanam dades rebudes
nombre = input( "Introdueix cadena de bits a enviar amb longitut multiple de 4: " )
qbits = 4

# Convertim cadena de texte en llista agrupada de 4 bits
lista = convertir2(nombre,qbits)
print( "Paquets de dades a enviar:" )
print( lista )

# Codificam paquets amb Hamming(7,4)
codificat = hamming4( lista )
print( "Paquets codificats. Afegim un paquet erroni 1001010 (valor 10):" )
codificat.append( "1001010")
print( codificat )

# Decodificam informació rebuda
decodificat = decodifica( codificat )
print( "Paquets decodificats i corregits:")
print( decodificat )

# Per millorar, imprimir valors rebuts.




