import math

acabar = False


print ("Escriu la sequència de naturals. Escriu 0 per acabar la llista:") 
while ( not acabar  ):
    nombre = int ( input("Nombre? ") )
    if ( nombre == 0 ):
        acabar = True
    else:
        print(" El nombre al cuadrat és " + str( nombre*nombre ) + ". La arrel és " + str( math.sqrt( nombre ) ) )
