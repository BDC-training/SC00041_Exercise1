My_file = "/Users/xidega/SC00041_Exercise1-group4/sample.txt" # Defining file path  

f = open(My_file) # open file at path

print(f.read()) # print the contents of the file to get an overview

print("Line\tChars\tUppercase\t% Upper") # print column names for table

f = open(My_file) # open file again
i = 1 # define iteration variable i
for l in f:
    total = len(l.strip()) #Number of characters of row
    upper = 0
    for c in l:
        if c.isupper(): # Number of uppercase letters in row
            upper += 1
    if total != 0:
        p = upper / total * 100 # Calculating what proportion of all characters are uppercase then multiolyign by 100 to get as percent.
    else:
        p = 0
    print(str(i) + "\t" + str(total) + "\t" + str(upper) + "\t" + str(round(p, 2)) + "%") #print data calculated above.
    i += 1

