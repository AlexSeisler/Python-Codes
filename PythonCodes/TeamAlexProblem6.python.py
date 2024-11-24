def Bikerentals(a,x,b,y,T):
    totala=0
    daypaya=0
    daypaya=(T-30)
    if daypaya>0:
        daypaya=daypaya*x
        daymontha=daypaya*21
    else:
        daymontha=0
    totala=daymontha+a
    totala=round(totala)
    
    
    totalb=0
    daypayb=0
    daypayb=(T-45)
    if daypayb>0:
        daypayb=daypayb*y
        daymonthb=daypayb*21
    else:
        daymonthb=0
    totalb=daymonthb+b
    totalb=round(totalb)
    
    return ("Total A: "+str(totala)+" Total B: "+str(totalb))


user=input("feeA, amountextraA,feeB,amountextraB,Time:   ")
user=user.split(" ")
print(Bikerentals(float(user[0]),float(user[1]),float(user[2]),float(user[3]),float(user[4])))