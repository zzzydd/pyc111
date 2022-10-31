#建立一個要儲存資料的串列變數 
data = list()

#開啟檔案
f = open("bodyinfo.txt", "r", encoding="utf-8")
#把檔案以列為區分，全部讀入之後再放到串列變數mydata中
mydata = f.readlines()
f.close()
#把第0列的欄位名稱以逗號剖開之後，再分別放入k0~k2變數中
k0, k1, k2 = mydata[0].split(",")
#以下用來移除k0~k2字串變數前後的符號以及多餘的空白
k0 = k0.strip()
k1 = k1.strip()
k2 = k2.strip()
#從第1列開始讀取所有的資料，分別放到d變數中
for d in mydata[1:]:
    #把字串變數d，以逗號剖開字串，放到sd這個串列變數中
    sd = d.split(",")
    #建立一個暫存的字典變數
    temp = dict()
    #分別以k0~k2的欄位名稱放入整理過後的資料（name, height, weight)
    temp[k0] = sd[0].strip()
    temp[k1] = float(sd[1].strip())
    temp[k2] = int(sd[2].strip())
    #把字典變數temp附加到data串列中
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