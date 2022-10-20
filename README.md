#llegir
#mirar si es nombre
#mirar si vel nombre es 0-255
#mostrar missatge
def llegirIP():

    print("Escriu una IP")
    x = input()
    return x

def nombreValid(nombre):

    if (ip >= 0) and (ip <= 255):
        return True
    else:
        return False

def comprovaIP(x):
    x = x.split(".")
    print(x)
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    if (nombreValid(a) and nombreValid(b) and nombreValid(c) and nombreValid(d)):
        print("És una IP vàlida. ", ip)
        return True
    else:
        print("És una IP no vàlida", ip)
        return False
    
sortir = false
#llegir ip sencera (192.168.1.2)
while not sortir:
    ip = llegirIP()
    #la dividim en 4 parts (a=192 ; b=168 ; c=1 ; d=2)
    #comprovar tots els trossos amb nombreValid()
    if ip != 'sortir'
        comprovaIP(ip)
    else:
        sortir = True
        #nombreValid(ip)
print("Ha acabat l'execució")
