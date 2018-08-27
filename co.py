n=int(input())
m=int(input())
mainlist=[]
for i in range(n):
    lis=[]
    for j in range(m):
        a,b=input().split()
        b=float(b)
        lis.append({a:b})
    mainlist.append(lis)
print("mainlist is {}".format(mainlist))
count = 0
while count<m*n:
    marks=-1
    j=0
    index=-1
    for i in mainlist:
        if i==[]:
            pass
        else:
            if marks<list(i[0].values())[0]:
                marks=list(i[0].values())[0]
                index=j
        j=j+1
    if index!=-1:
        print(list(mainlist[index][0].keys())[0],list(mainlist[index][0].values())[0])
        mainlist[index].pop(0)
    count=count+1
