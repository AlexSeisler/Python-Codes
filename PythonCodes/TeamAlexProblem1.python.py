def gymmembership(monthlyfee,anualfee,tax,vpy):
    totalall=(monthlyfee*12)+anualfee
    tax=(tax/100)+1
    taxedtotal=totalall*tax
    totalmonthly=taxedtotal/12
    totalmonthly=format(totalmonthly,".2f")
    cpv=taxedtotal/vpy
    cpv=format(cpv,".2f")
    if totalmonthly == "0.00":
        totalmonthly = 0
    if cpv == "0.00":
        cpv = 0
    return (str(totalmonthly)+" "+str(cpv))
user=input("monthlyfee annualfee tax vpy: ")
user=user.split(" ")
print(gymmembership(float(user[0]),float(user[1]),float(user[2]),float(user[3])))