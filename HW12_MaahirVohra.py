# Maahir Vohra
# CS100 Section 008
# HW 12, April 27, 2023

''' Problem 1 '''


def safeOpen(filename):
    try:
        return open(filename)
    except FileNotFoundError:
        return None


''' Problem 2 '''


def safeFloat(x):
    try:
        return float(x)
    except ValueError:
        return 0.0


''' Problem 3 '''


def averageSpeed():
    # open the file using safeOpen giving user 2 tries to enter a correct file name before stopping the program
    attempts = 0
    while attempts < 2:
        filename = input("Please enter the filename: ")
        oFile = safeOpen(filename)
        if oFile is None:
            print("File not found. Please try again.")
            attempts += 1
        else:
            break
    else:
        print("File not found. Yet another human error. Goodbye.")
        return

# strip and split each speed and append to speedList if it passes safeFloat()
    speedList = []
    try:
        for line in oFile:
            strippedSpeed = line.strip().split()
            for speed in strippedSpeed:
                safeSpeed = safeFloat(speed)
                if safeSpeed > 2:
                    speedList.append(safeSpeed)
    except ValueError:
        pass
    oFile.close()

# calculate the average speed
    average = sum(speedList) / len(speedList)
    print("Average speed is", average, "miles per hour.")


averageSpeed()
