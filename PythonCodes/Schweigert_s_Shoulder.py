import math
def shoulder(p1,p2,a,vi):
    
    distance=math.sqrt(math.pow(((p2[0]-p1[0])),2)+math.pow((p2[1]-p1[1]),2))

    acceleration=a
    initial=vi
    
    vf=math.sqrt(math.pow(initial,2)+2*acceleration*distance)

    time=round(((vf-initial)/acceleration),3)
    
    return ("Schweigert has "+str(time)+" seconds left.")
    
print(shoulder([12,4],[5,5],3,6))
print(shoulder([4,4],[5,5],1,15))
print(shoulder([9,8],[3,19],4,12))
print(shoulder([2,9],[5,5],3,4))
print(shoulder([0,0],[0,0],5,0))
print("")
print(shoulder([3,3],[9,9],2,10))
print(shoulder([7,3],[11,10],6,4))
print(shoulder([2,1],[8,8],2,0))
print(shoulder([8,7],[2,2],5,9))
print(shoulder([5,19],[6,4],6,12))