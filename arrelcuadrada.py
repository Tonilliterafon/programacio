import math


txt =("el nombre {} quadrat és {} i arrel {:6f}")
#llista buida
llista=[]
#aixó és un token
acabar = False

print ("Escriu la sequència de naturals. Escriu 0 per acabar la llista:") 
while ( not acabar  ):

    nombre = int(input("Nombre: "))
    if nombre == 0:
        acabar = True
    else:
        llista.append(nombre)
print(llista)

for nombre in llista:
    print(txt.format (nombre,nombre*nombre,math.sqrt(nombre)))
"""
while ( acabar = True  ):
    
    if ( nombre == 0 ):
        acabar = True
    else:
        #print(" El nombre al cuadrat és " + str( nombre*nombre ) + ". La arrel és " + str(( math.sqrt( nombre )) ) )
        
        print(txt.format (nombre,nombre*nombre,math.sqrt(nombre)))
"""
