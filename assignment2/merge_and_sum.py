def merge_and_sum(d1, d2):
    result=d1.copy()
    for key, value in d2.items():
        result[key]=result.get(key,0)+value
    return result
d1={
    'a':10,
    'b':20,
    'c':30
}
d2={
    'b':5,
    'c':15,
    'd':40
}
print(merge_and_sum(d1, d2))