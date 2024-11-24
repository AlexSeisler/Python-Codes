def cut(massege,key):
    ans=""
    end=[]
    length=len(massege)
    ans=key
    while True:
        if len(massege)> len(ans):
            ans=ans+key
        else:
            break
    x=len(massege)
    ans=ans[:x]

    ans=list(ans)
    for i in range(len(ans)):
        if ans[i].isupper():
            ans[i]=ord(ans[i])
            ans[i]=ans[i]-65
        elif ans[i].islower():
            ans[i]=ord(ans[i])
            ans[i]=ans[i]-97

    massege=list(massege)
    while True:
        user=input("1: Encrypt or 2: Decrypt?")
        if user=="1":
            for i in range(len(ans)):
                end.append(((ord(massege[i])+(ans[i]))))
            break
        elif user=="2":
            for i in range(len(ans)):
                end.append(((ord(massege[i])-(ans[i]))))
            break
        else:
            print("Incorrect input")
            continue
        




    for i in range(len(end)):
        if massege[i].isalpha():
            while True:
                if massege[i].isupper():
                    if end[i] > 90:
                        end[i]=end[i]-26
                    elif end[i]<65:
                        end[i]=end[i]+26
                    elif end[i]>64 and end[i]<91:
                        end[i]=chr(end[i])
                        break

                

                elif massege[i].islower():
                    if end[i]>122:
                        end[i]=end[i]-26
                    elif end[i]<97:
                        end[i]=end[i]+26
                    elif end[i]>96 and end[i]<123:
                        end[i]=chr(end[i])
                        break

        else:
            end[i]=chr(end[i])
    return end
    
message=input("What is your message: ")
key=input("What is your key: ")
print(cut(message,key))