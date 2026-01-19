list1=[1,2,3,4,5]
lsit1=tuple(list1)
print(f"Original tuple is: {list1}")
for i in range(len(list1)//2):
    temp=lsit1[i]
    list1[i]=list1[-(i+1)]
    list1[-(i+1)]=temp
print(f"Reversed tuple is: {list1}")