a = list('甲乙丙丁')*6
b = list('子丑寅卯辰巳午未申酉戌亥')*5
x = zip(a,b)
for t in x:
    print(t[0]+t[1])