import csv

with open("TestData/result.csv" , "r") as file:

    reader = csv.reader(file)

    next(reader) ## Skip the header

    # for row in reader:
    #     print(row)

    # To skip the header row

    for column in reader:

        username = column[0]   # column 1
        password = column[1]   # column 2

        print(username, password)

