count=0
def count_ways(target_sum,num_denominations,denominations):
    for i in range(num_denominations):
        if target_sum!=0 and target_sum>0:
            denomination=denominations[i]
            target_sum=target_sum-int(denomination)
            return count_ways(target_sum,num_denominations,str(denomination))
        elif target_sum==0:
            global count
            count=count+1
    return count   
    

            





user=input("target amount denominations: ")
user=user.split(" ")
print(user)
target_sum=int(user[0])
num_denominations=int(user[1])
denominations=[]
for i in range(num_denominations):
    denominations.append(str(user[i+2]))

print(target_sum)
print(num_denominations)
print(denominations)
print(count_ways(target_sum,num_denominations,denominations))






"""
def count_ways(target_sum,num_denominations,denominations):
    dp=[]
    for i in range(target_sum+1):
        dp.append([0])
    dp[0]=1
    
    for denomination in denominations:
        for i in range(denomination,target_sum+1):
            dp[i]+=dp[i-denomination]
    return dp[target_sum]

user=input("target amount denominations: ")
user=user.split(" ")
print(user)
target_sum=int(user[0])
num_denominations=int(user[1])
denominations=[]
for i in range(num_denominations):
    denominations.append(int(user[i+2]))

print(target_sum)
print(num_denominations)
print(denominations)
print(count_ways(target_sum,num_denominations,denominations))

"""