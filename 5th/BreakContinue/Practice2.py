tup=(1,4,9,16,25,36,49,64,81,100)
x=9
i=0
for gand in tup:
    if(gand==x):
        print("Found at index",i)
        break
    i+=1
    print(i)