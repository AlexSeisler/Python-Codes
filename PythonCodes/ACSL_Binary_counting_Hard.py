import sys
count=-1
def Counting(string):
    binary=""
    zero="0"
    for i in range(len(string)):
        adder=(bin(ord(string[i]))[2:])
        while True:
            if len(adder)<8:
                adder=zero+adder
            else:
                break
        binary=binary+adder
    return binary
   
def remove(binary):

    global count
    count=count+1
    counting=["0","1","10","11","100","101","110","111","1000","1001","1010","1011","1100","1101","1110","1111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001","11010","11011","11100","11101","11110","11111"]
    sequence=counting[count]
    find=binary.find(sequence)
    if find==-1:
        print(int(counting[count-1],2))
        sys.exit(0)

    binary=binary[:find]+binary[find+len(counting[count]):]
    binary=binary[::-1]
    sequence = sequence[::-1]
    find=binary.find(sequence)
    if find==-1:
        binary = binary[::-1]
        return binary
    binary=binary[:find]+binary[find+len(counting[count]):]
    binary=binary[::-1]
    return binary
    

    
        
    
#Roses are red.     
#A is Alpha; B is Bravo; C is Charlie. 
#A stitch in time saves nine.
#1, 2: Buckle my shoe! 3, 4: Shut the door!
#Is HackerRank the platform used by ACSL?

binary_string=(Counting("Lions and Tigers and Bears, Oh My! This is from The Wizard of Oz."))

while True:
    binary_string =remove(binary_string)