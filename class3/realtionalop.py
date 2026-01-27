list1=[1,2,3,4,5,6]
avg=0
for x in list1:
    avg+=x
avg/=len(list1)
count=0
for x in list1:
    if avg > x:
        count+=1
print(f"average is {avg}, number of elements greater than average: {count}")