#predicted output: 48  due to operator precedence **> "*=/" > "+=-" the equal parts are left to right precedence
print(10 +5 * 2 ** 3 -4 /2)
#so first exponent 10 + 5 * 8 - 4 / 2
# then mul and div but left first so mul
# 10 + 40 - 4 / 2
# now div 10 + 40 - 2
#now left to right 48
