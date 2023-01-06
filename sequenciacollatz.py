import math

passos = 0
nombre = int ( input("Introdueix nombre. Escriu 0 per acabar: ") )
while ( nombre != 1 ):
    if ( nombre % 2 == 0 ):
        nombre = nombre / 2
    else:
        nombre = ( nombre * 3 ) + 1
    passos += 1

print( "Passos = " + str( passos) )
