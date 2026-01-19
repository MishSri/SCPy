import sys
list1=[11,5,16,18,24,3,88]
largest=-sys.maxsize-1
smallest=sys.maxsize
for i in list1:
    if(i>largest):
        largest=i
    if i<largest:
        smallest=i
print(f"Largest number in the list is {largest}")
print(f"Smallest number in the list is {smallest}")