# fabio bonini

x = int(input("please enter a int number: "))

print (int(x))

while x > 1:
    if x % 2 == 0: 
        x = x / 2
        print (int(x))
    else: 
        x = (x * 3) + 1        
        print (int(x))


print ("and finish!!!")