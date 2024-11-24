
alpha="asdfghjklqwertyuiopzxcvbnmASDFGHJKLXCVBNMQWERTYUIOP1234567890"#maybe more of them keep in mind
occurrence=1
result=""



def replace_punctuation(text):
    punctuation_list = [".  ", "!  ", "?  "]
    special=[" - ","/",", ","-"]
    for i in range(len(text)):
        try:
            if alpha.find(text[i]) ==-1:
                special.append(text[i])
            if alpha.find(text[i]) ==-1 and alpha.find(text[i+1])==-1:
                special.append(text[i]+text[i+1])
            if alpha.find(text[i]) ==-1 and alpha.find(text[i+1])==-1and alpha.find(text[i+2])==-1:
                special.append(text[i]+text[i+1]+text[i+2])
        except:
            continue
            
    
    for punctuation in punctuation_list:
        text = text.replace(punctuation, "Z")
        
    for spec in special:
        text = text.replace(spec, " ")
    return text
def find_occurrence(Letter, Occurrence, Sentences):
    oc_count=0
    

    for i in range(len(Sentences)):
        keep = Sentences[i].split()

        for j in range(len(keep)):
            word = keep[j]
            for k in range(len(word)):
                char = word[k]
                
                if char == Letter:
                    oc_count=oc_count+1
                    if oc_count==Occurrence:
                        return str(i+1)+"."+str(j+1)+"."+str(k+1)

      

    return -1
    
    
    
    
def swc(letter,theText):
    mod_occurrence=occurrence
    
    while(True):
        if find_occurrence(letter, mod_occurrence, theText)==-1:
            mod_occurrence=mod_occurrence//2
        else:
            return str(find_occurrence(letter, mod_occurrence, theText))
    
        
    
    
def encodeMessage(text, message):
    global occurrence
    global result
    text1=replace_punctuation(text)
    text1=text1.split("Z")
    for i in range(len(message)):
        
        if alpha.find(message[i])!=-1:
            keep=swc(message[i],text1)
            occurrence=occurrence+1
            if(message[i+1]==" "):
                result=result+str(keep)
            elif(alpha.find(message[i+1])==-1):
                result=result+str(keep)
            else:
                result=result+str(keep)+" "
        elif(message[i]==" "):
            result=result+"_"
        else:
            result=result+message[i]
    
    return result