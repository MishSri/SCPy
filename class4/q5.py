def fibo(num):
    if num==0 or num==1:
        return 1
    return fibo(num-1)+fibo(num-2)
num=5
print(f"The {num}th fibonacci number is: {fibo(num)} ")
# in exam operator precedence, simple functions, basic theory