tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)
ans=[]
for x in range(len(tuple1)):
        ans.append(tuple1[x]+tuple2[x])
ans=tuple(ans)
print(ans)

