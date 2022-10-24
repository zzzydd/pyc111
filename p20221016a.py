'''
for i in range(3):
    chi = int(input("chi="))
    eng = int(input("eng="))
    total = chi + eng
    avg = total / 2
    print(total, avg)
chi = int(input("chi="))
while chi >= 0:
    eng = int(input("eng="))
    total = chi + eng
    avg = total / 2
    print(total, avg)
    chi = int(input("chi="))
print("Thank you, bye!")
'''

data = list()
score = int(input("Score="))
while score >=0 :
    data.append(score)
    score = int(input("Score="))
print("Sum=", sum(data))
print("Average=", sum(data)/len(data))
print("Max=", max(data))
print("Min=", min(data))