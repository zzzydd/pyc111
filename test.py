a = list('甲乙丙丁戊己庚辛壬癸')*6
b = list('子丑寅卯辰巳午未申酉戌亥')*5
x = zip(a,b)
for t in x:
    print(t[0]+t[1], end=" ")