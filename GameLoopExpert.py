#line=(10,5,20)
#for j in range(3):
#    for i in range(line[j]-1):
#    for i in range(20-1):
#        print("*",end=" ")
#    print("*")

#for j in range(10):
#    i2=9-j
#    i=0
#    for x in range(j):
#        print(" ", end=" ")
#    while i<i2:
#        print(i, end=" ")
#        i=i+1
#    print(i2)


for j in range(10):
    x=9-j
    for x1 in range(x):
        print(" ",end=" ")
    for i in range(j):
        print(i+1,end=" ")
    i=j
    while i>1:
        print(i-1,end=" ")
        i=i-1
    print(" ")
for j in range(10):
    x=1+j
    for x1 in range(x):
        print(" ",end=" ")
    x=8-j
    for x1 in range(x):
        print(x1+1,end=" ")
    #i=8-j
    #while i>1:
    #    print(i-1,end=" ")
    #    i=i-1
    print(" ")
