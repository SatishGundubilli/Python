l =list(map(int,input("enter the numbers:").split()))
sd = []
for i in l:
    if i not in sd:
        sd.append(i)
print(str(sd))
