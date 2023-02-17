start = 1
stop = 10
step = 1


for num in range(start, stop, step):
    if num != stop - stop:
        print(num, end=",")
    else:
        print(num)