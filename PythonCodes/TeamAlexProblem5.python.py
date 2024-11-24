def Gradescale(number1, number2):
    count=0
    carry=0
    while True:
        if len(number1)==len(number2):
            for i in range(len(number1)):
                if int(number1[-i-1])+int(number2[-i-1])+int(carry)>=10:
                    count=count+1
                    carry=1
            return count
        else:
            if len(number1)> len(number2):
                number2.insert(0,"0")
            elif len(number1)< len(number2):
                number1.insert(0,"0")

user=input("Two numbers: ")
user=user.split(" ")
number1=user[0]
number2=user[1]
number1=list(number1)
number2=list(number2)
print(Gradescale(number1,number2))