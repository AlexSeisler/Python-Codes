import math
def amount(days,model,insurance,miles,fuel):
    Daily=0
    Weekly=0
    GasTank=0
    count=0
    base=0
    extra=0
    
    if days%1>.1:
        days=math.ceil(days)
    else:
        days=math.floor(days)
    
    
    if days*150<miles:
        extra=miles-days*150
        extra=extra*.25
        base=base+extra
    if insurance==1:
        base=base+(9.95*days)
    if model==1:
        Daily=19.95
        Weekly=66.96
        GasTank=12
    elif model==2:
        Daily=23.95
        Weekly=76.95
        GasTank=16
    elif model==3:
        Daily=28.95
        Weekly=86.95
        GasTank=18
    elif model==4:
        Daily=31.95
        Weekly=94.95
        GasTank=20
    elif model==5:
        Daily=35.95
        Weekly=99.95
        GasTank=24
    
    while True:
        if days >=7:
            days=days-7
            count=count+1
        elif days ==6:
            days=days-6
            count=count+1
        elif days==5:
            days=days-5
            count=count+1
        else:
            break
    base=base+((count*Weekly)+(days*Daily))
    if fuel!=1:
        fuel=1-fuel
        GasTank=GasTank*fuel
        GasTank=GasTank*1.32
        base=base+GasTank
    
    return base
    
print(amount(3,2,1,400,1.0))
print(amount(6,3,0,500,.5))
print(amount(8.05,1,1,1300,.25))
print(amount(11,5,1,2000,.4))
print(amount(15.62,4,1,3000,.75))
print("")
print(amount(4,1,0,300,1))
print(amount(5,2,1,400,.5))
print(amount(9,3,1,1400,.4))
print(amount(13.02,4,1,2100,.3))
print(amount(16.5,5,1,3000,.75))