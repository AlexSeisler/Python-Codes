def Battery(time,level):
    if level>20:
        levelupper=(level-20)/1
        levellower=(level-levelupper)/.5
        totaltime=levelupper+levellower
    else:
        totaltime=level/.5
    return totaltime
    
user=input("time level:    ")
user=user.split(" ")
print(Battery((float(user[0])),float(user[1])))