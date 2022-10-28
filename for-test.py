data = [1, 2, 3, 4, 5, 6]
data1 = list("abcdef")

data2 = zip(data, data1)
for item in data2:
    print(item)

print(data)
print(data1)