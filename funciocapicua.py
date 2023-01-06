def es_capicua( n ):
    nocapi = True
    capicua = str( n )
    primera = 0
    darrera = len( capicua ) - 1
    while ( primera <= darrera ):
        if ( capicua[primera] != capicua[darrera] ):
            nocapi = False
        primera += 1
        darrera -= 1
        
    return nocapi
