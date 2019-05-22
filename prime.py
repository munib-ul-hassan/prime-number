a = int (input ("Input your value: "))
for i in range (2,a):
    if (a % i) == 0:
        print ("this is not a prie number")
        break
else:
    print ("this is  prime number")
