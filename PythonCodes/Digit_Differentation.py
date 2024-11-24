def binary(x):
    total=0
    total1=0
    ans=""
    ans1=0
    print("Input: "+str(x))
    x=bin(x)
    x=x[2:]
    print("Binary Representation: " +str(x))
    x=list(x)

    for i in range(len(x)):
        if x[i]=="1":
            total=total+1
        if x[i]=="0":
            total1=total1+1
    if total>total1:
        ans="More"
        ans1=total-total1
    elif total<total1:
        ans="LESS"
        ans1=total1-total
    else:
        ans="EQUAL"
        ans1=0
    
    print("Count of 1's: "+str(total))
    print("Count of 0's: "+str(total1))
    print("Absolute Difference: "+str(ans)+" "+str(ans1))
"""
binary(1880)
print("")
binary(4216)
print("")
binary(420)
print('')
binary(6104)
"""
binary(1)
binary(8191)
binary(3276)
binary(1738)
binary(5637)