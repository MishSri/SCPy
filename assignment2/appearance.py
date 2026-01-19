tup1=(1,1,2,5,3,2,5,4)
set1=set(tup1)
cnt=0
for i in set1:
    for j in tup1:
        if i == j:
            cnt+=1
    print(f"{i} appearsm {cnt} number of times in tuple")
    cnt=0

