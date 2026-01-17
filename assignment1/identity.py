#Two list with same value
list1=[1,2,3]
list2=[1,2,3]
if list1 is list2:
    print('They are same')
else:
    print("It is not identity.")
 #referencing sam eobject
list2=list1
if list2 is not list1:
    print("Not identity")
else:
    print("they are same.")
