def Mut(x):
    Letters=list(x)
    for i in range(len(Letters)):
        if i==0:
            continue
        if i%5==0:
            if Letters[i]=="a" or Letters[i]== "A" or Letters[i]== "e" or Letters[i]== "E" or Letters[i]== "i" or Letters[i]== "I" or Letters[i]== "o" or Letters[i]== "O" or Letters[i]== "u" or Letters[i]== "U":
                Letters[i]=""
        if i%3==0:
            Letters[i]="*"
        if i%2==0:
            if Letters[i].isupper():
                Letters[i]=Letters[i].lower()
            elif Letters[i].islower():
                Letters[i]=Letters[i].upper()
        
    Letters="".join(Letters)
    return Letters
        
        
    
    
print(Mut("PhYSIcsPHridaY"))
print("")
print(Mut("bloomsburgcodingcompetition"))
print("")
print(Mut("aBcDeFGHIjkLmnOp"))
print("")
print(Mut("COmpuTeRScIenCEONe"))
print("")
print(Mut("PYTHONisCOOL"))
print("")
print(Mut("bInaRYhexOCTal"))
print("")
print(Mut("CODING"))
print("")
print(Mut("aeiouaeiouaeiouaeiou"))
print("")
print(Mut("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv"))
print("")
print(Mut("THeeYAzmAN"))
print("")
print(Mut("ELtoroTHEbull"))
print("")
print(Mut("IhOpEyOuGeTtHiSrIgHt"))
print("")
print(Mut(""))