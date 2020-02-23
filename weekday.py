# fhbonini
# program to answer if it's a weekday or weekend

import datetime
n = datetime.datetime.now()
n = n.weekday()

if n < 5:
    print ("today is a weekday")
else:
    print ("today is a weekend")


#print (n)