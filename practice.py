<<<<<<< HEAD
=======
def readAge(filename):
    strAge = None
    while True:
        try:
            if strAge == None:
                infile = open(filename)
                strAge = infile.readline()
            age = int(strAge)
            print('Next year you will be', age+1)
            break
        except ValueError:
            print('Value cannot be converted to integer.')
            strAge = input("Enter your age in digits: ")
        except FileNotFoundError:
            print('Input file is missing:', "'" + filename + "'")
            filename = input("Enter a correct file name: ")


readAge('inputfile.txt')
#fix the above code so that it doesn't merely output an error message
>>>>>>> e8617ac76e47f891b08f5e276fc029be608f6b95
