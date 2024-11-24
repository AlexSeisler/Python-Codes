def Compoundinterest(deposit, term, rate):
    rate=rate/100
    Amount=(deposit*((1+rate/12)**(12*term)))
    Amount=format(Amount,".2f")
    return (("Amount after compounding: "+str(Amount)))
    
    
    
user=input("deposit term rate: ")
user=user.split(" ")
print(Compoundinterest(float(user[0]), float(user[1]), float(user[2])))