data = list()
n = input("num=")
for i in range( int(n) ):
    s = input("score=")
    data.append( int(s) )
print("最高分：",max(data))
print("最低分：",min(data))
print("平均：", sum(data)/len(data))
