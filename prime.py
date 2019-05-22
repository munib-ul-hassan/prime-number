a = int (input ("Input your value: "))
b = 0
for i in range (2,a-1):
    if (a % i) == 0:
        print ("this is not a prie number")
        break
else:
    print ("this is  prime number")
