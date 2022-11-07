file = "p.txt"

fp = open(file, "r", encoding="utf-8")
data = fp.readlines()
fp.close()

print(data[0].strip().split("：")[1], end="")
print(data[1].strip().split("：")[1])
for line in data[2:]:
	print(line.strip())