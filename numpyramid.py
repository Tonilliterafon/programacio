#for z in range (11):
    #for t in range(z):
        #print(t, end="")
    #print(" ")


#for y in range (10):
    #for x in range (10-y):
        #print(x,end="")
    #print(" ")

for k in range (1,10):
    for l in range (1,10):
        if (l*k) < 10:
            print("0" ,end="")
        print(l*k ,end=" ")
    print(" ")
