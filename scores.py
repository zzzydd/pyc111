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
    print("6. Save scores to a file")
    print("7. Load scores form a file")
    print("0. End the program")
    print("------------------")
    res = input("Please input your choice:")
    if res == "1":
        data.clear()
        names.clear()
    elif res == "2":
        s = int(input("Score(-1 to end)="))
        while s>0:
            n = input("Name=")
            data.append(s)
            names.append(n)
            s = int(input("Score(-1 to end)="))
    elif res == "3":
        n = input("Name=")
        try:
            i = names.index(n)
            del names[i]
            del data[i]
        except:
            pass
    elif res == "4":
        print("Max score is ", max(data))
        print("Min score is ", min(data))
        print("Average score is ", round(sum(data)/len(data),2))
    elif res == "5":
        score_table = zip(names, data)
        for item in score_table:
            print(item)
    elif res == "6": # save the scores to a file
        filename = input("Filename:")
        fp = open(filename, "w", encoding="utf-8")
        score_table = zip(names, data)
        for item in score_table:
            fp.write(item[0]+","+str(item[1])+"\n")
        fp.close()
    elif res == "7": # load the scores from a file
        filename = input("Filename:")
        fp = open(filename, "r", encoding="utf-8")
        rawdata = fp.readlines()
        fp.close()
        names.clear()
        data.clear()
        for item in rawdata:
            names.append(item.split(",")[0])
            data.append(int(item.split(",")[1]))
    elif res == "0":  # quit the program
        quit = True
    else:
        print("I can't recognize your command!")