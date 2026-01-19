dict1={
    "a":3,
    "b":2,
    "c":1
}
sorted_dict1=dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_dict1)