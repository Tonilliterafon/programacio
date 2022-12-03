def sumaUnSegon(h,m,s):
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24: 
                h = 0
    return [h,m,s]

def sumaUnSegon2(h,m,s):
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24: 
                h = 0
    if ( h < 10 ):
        hora = '0' + str(h)
    else:
        hora = str(h)
    if ( m < 10 ):
        min = '0' + str(m)
    else:
        min = str(m)
    if ( s < 10 ):
        sec = '0' + str(s)
    else:
        sec = str(s)
        
    cadena = hora + ":" + min + ":" + sec
    return cadena

#QUE SURTI AMB FORMAT 00:00:00
print(sumaUnSegon2(1,2,59))
print(sumaUnSegon2(23,59,59))
print(sumaUnSegon2(0,59,59))
