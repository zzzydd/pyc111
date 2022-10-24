quit = False
data = list()
names = list()
while not quit:
    print("----Welcome-------")
    print("1. Clear data")
    print("2. Input score")
    print("3. Remove student's data")
    print("4. Print the Average/Max/Min data for the scores")
    print("5. List all students' data")
    print("6. End the program")
    print("------------------")
    res = input("Please input your choice:")
    if res == "1":
        data.clear()
        names.clear()
    elif res == "2":
        s = int(input("Score="))
        n = input("Name=")
        data.append(s)
        names.append(n)
    elif res == "3":
        n = input("Name=")
        i = names.index(n)
        del names[i]
        del data[i]
    elif res == "4":
        print("Max score is ", max(data))
        print("Min score is ", min(data))
        print("Average score is ", round(sum(data)/len(data),2))
    elif res == "5":
        score_table = zip(names, data)
        for item in score_table:
            print(item)
    elif res == "6":
        quit = True
    else:
        print("I can't recognize your command!")