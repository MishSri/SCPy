list1=[1,2,3,4,5, 55, 67]
thisdict={}
for i in list1:
    if i%2==0:
        thisdict.update({f"{i}": "even"})
    else:
        thisdict.update({f"{i}": "odd"})

print(thisdict)