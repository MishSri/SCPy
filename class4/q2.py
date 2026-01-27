num=13
i=2
while i<num:
    if num%i==0:
        print("It is not a prime number.")
        break
    i+=1
else:
    print("It is a prime number.")