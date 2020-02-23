# fabio h bonini
# program to return the squareroot

#def sqrt(x):
#    y = 1
#    cont = 0
#    while x > 0:
#        x = x - y
#        y = y + 2
#        cont = cont + 1
#    else:
#        print ("The square root is approx. ", cont)
    
def sqrt (x):
    x= x**(0.5)
    print ("The square root is ", x)

x = float(input("Enter a positive number: "))
sqrt(x)