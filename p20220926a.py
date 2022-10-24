url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for pg in range(1, 51):
    u = url.format(pg)
    print(u)