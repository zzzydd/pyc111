data = list()

f = open("bodyinfo.txt", "r", encoding="utf-8")
mydata = f.readlines()
f.close()
k0, k1, k2 = mydata[0].split(",")
k0 = k0.strip()
k1 = k1.strip()
k2 = k2.strip()
for d in mydata[1:]:
    sd = d.split(",")
    temp = dict()
    temp[k0] = sd[0].strip()
    temp[k1] = float(sd[1].strip())
    temp[k2] = int(sd[2].strip())
    data.append(temp)

# data input by yourself
# name = input("Your name:")
# while name!="":
#     h = float(input("Your height:"))
#     w = int(input("Your weight:"))
#     temp = dict()
#     temp["name"] = name
#     temp["height"] = h
#     temp["weight"] = w
#     data.append(temp)
#     name = input("Your name:")

for d in data:
    name = d["name"]
    h = d["height"]
    w = d["weight"]
    bmi = w / h**2
    print("{}的身高：{}公分，體重：{}公斤，你的BMI是：{}".format(
        name, h*100, w, round(bmi,2)))