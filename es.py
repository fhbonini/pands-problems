# Fabio Bonini
# programm to count the e's

import sys

def counte():
    count = 0
    vocal=["e"]
    for i in vocal:
        for j in contents:
            if (i==j):
                count+=1
    print (count)



with open(sys.argv[1], 'r') as f:
    contents = f.read()
    counte()

#    print(x)
# print (contents)




