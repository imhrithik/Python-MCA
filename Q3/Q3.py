def divisible_by_7_not_5(start, end):
    for i in range(start, end+1):
        if (i % 7 == 0 and i % 5 != 0):
            print(i,end=" ")

divisible_by_7_not_5(1000, 2000)