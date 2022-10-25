data = list()

try:
    score = int(input("Score="))
except:
    score = -1
while score >=0:
    data.append(score)
    try:
        score = int(input("Score="))
    except:
        score = -1
if len(data)>0:
    print(data)
    print("Max:", max(data))
    print("Min:", min(data))
    print("Average:", sum(data)/len(data))
else:
    print("There is no any data here!")