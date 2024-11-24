class Course:
    def __init__(self,name="Unknown",credits=1,weight=1.0):
        self.credits=credits
        self.weight=weight
        self.name=name
    def __repr__(self):
        return("Course: "+str(self.name)+", Weighted: "+str(self.weight)+", Credits: "+str(self.credits))
class Student:
    def __init__(self,name,dictionary):
        self.name=name
        self.dictionary=dictionary
    def creditTotal(self,name,dictionary,Credits):
        total=0
        for key in self.dictionary:
            total=total+Credits[key]
        return ("Name: "+str(self.name)+" Total Credits: "+str(total))
    def __repr__(self):
        String=""
        for key in self.dictionary:
            String=String+" "+str(key)
        return ("Name: "+str(self.name)+" Classes:"+str(String))
    def GPA(self,dictionary,weights):
        total=0
        amount=0
        for key in dictionary:
            amount=amount+1
            point=0
            if dictionary[key]=="A":
                point=4.0
            elif dictionary[key]=="A-":
                point=3.67
            elif dictionary[key]=="B+":
                point=3.33
            elif dictionary[key]=="B":
                point=3
            elif dictionary[key]=="B-":
                point=2.67
            elif dictionary[key]=="C+":
                point=2.33
            elif dictionary[key]=="C":
                point=2
            elif dictionary[key]=="C-":
                point=1.67
            elif dictionary[key]=="F":
                point=0
            else:
                point=0
            total=total+(point*weights[key])
        total=total/amount
        return total
classes={"Physics":"A","Algebra":"A","Comp":"A"}
credits={"Physics":4,"Algebra":4,"Comp":8}
weights={"Physics":1.2,"Algebra":1.2,"Comp":1.2}
Alex=Student("Alex",classes)
#print(Alex.creditTotal("Alex",classes,credits))
print(Alex.GPA(classes,weights))