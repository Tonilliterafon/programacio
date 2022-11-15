import math

print("Introdueix nombres a calcular" )

linees = []
while ( linea := input() ):
	linees.append( linea )

for linea in linees:
	
	parcial = linea
	resultat = int(linea)
	longitut = len( linea )	
	while True:
	
		for i in range(longitut):
			if ( i == 0 ):
				resultat = int( parcial[0] )
			else:
				resultat = resultat * int( parcial[i] )
		print("EL producte dels digits de",str(parcial),"es",str(resultat),".")
		longitut = len( str(resultat) )
		parcial = str(resultat)		
		if ( longitut < 2 ):
			break	
	print("----------")
