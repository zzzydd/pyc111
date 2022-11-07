file = "news.txt"
fp = open(file, "r", encoding="utf-8")
data = fp.read()
fp.close()

q = input("Keywords:")
if q in data:
	print("{}在檔案中有找到".format(q))
	print("{}在檔案中出現了{}次".format(q, data.count(q)))
else:
	print("找不到！")
	