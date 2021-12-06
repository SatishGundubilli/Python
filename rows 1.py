n = int(input("enter the numbers:"))
for i in range(n):
    for j in range (n,0,-1):
        if j==i:
            print(1,end=' ')
     
        else:
            print(0, end = ' ')
        
    print()
