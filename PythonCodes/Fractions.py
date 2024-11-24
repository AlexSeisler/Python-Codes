"""
This code makes a class to represent and print a couple methods to call on 
fraction objects.
"""
#Brings in the use of certain math methods
import math
#Starts the class
class Fractions:
    #Uses the init method to take in instance variables
    def __init__(self,numerator=1,denominator=1):
        self.numerator=numerator
        self.denominator=denominator
    #repr method to print the output in good formating 
    def __repr__(self):
        return(str(self.numerator)+"/"+str(self.denominator))
    #Overides the equal sign
    def __eq__(self,other):
        return self.numerator==other.numerator and \
        self.denominator==other.denominator
    #Flips the numerator and denominator
    def reciprical(self):
        return Fractions(self.denominator,self.numerator)
    #Uses the gcd to find the simplified fraction and returns it as a new object
    def simplify(self):
        x=self.numerator
        y=self.denominator
        gcd=math.gcd(x,y)
        x=int(x/gcd)
        y=int(y/gcd)
        return Fractions(x,y)
    #Turns the fraction object into the decimal format
    def decimal(self):
        return float(self.numerator/self.denominator)
    #Multiplies the numerator by another integer and returns it as a new object
    def multiplyInt(self,other):
        x=self.numerator*other
        return Fractions(x,self.denominator)
    #Overrides the addition symbol to add the objects
    def __add__(self,other):
        denominator=self.denominator*other.denominator
        numerator=(self.numerator*other.denominator)+(other.numerator*self.denominator)
        return Fractions(numerator,denominator)
    #Overrides the multiplication symbol to multiply the objects
    def __mul__(self,other):
        numerator=(self.numerator*other.numerator)
        denominator=(self.denominator*other.denominator)
        return Fractions(numerator,denominator)
    #Overrides the subtraction symbol to subtract the objects
    def __sub__(self,other):
        denominator=self.denominator*other.denominator
        numerator=(self.numerator*other.denominator)-(other.numerator*self.denominator)
        return Fractions(numerator,denominator)
    #Overrides the division symbol to divide the objects
    def __truediv__(self,other):
        numerator=(self.numerator*other.denominator)
        denominator=(self.denominator*other.numerator)
        return Fractions(numerator,denominator)
#sets four fraction objects
f1=Fractions(15,20)
f2=Fractions(3,4)
f3=Fractions(7,8)
f4=Fractions(15,20)
#Prints all ways demonstrating the built fraction class.
print("-------------------------------------------------------------")
print("Uses the __init__ method to call 3 objects.f1-(15,20) f2-(3,4) f3(7,8),f4(15/20)")
print("Fraction(f1): "+str(f1))
print("Fraction(f2): "+str(f2))
print("Fraction(f3): "+str(f3))
print("Fraction(f4): "+str(f4))
print("-------------------------------------------------------------")
print("Uses an __eq__ method to compare two objects returns a boolean")
print("if they are equal returns true, else false")
print("Fraction 1 (15/20) = Fraction 2 (3/4): "+ str(f1==f2))
print("Fraction 2 (3/4) = Fraction 3 (7/8): "+ str(f2==f3))
print("Fraction 1 (15/20) = Fraction 4 (15/20): "+str(f1==f4))
print("-------------------------------------------------------------")
print("Uses a method to take in a fraction object and return the reciprical fraction object")
print("Reciprical of 15/20: "+str(f1.reciprical()))
print("Reciprical of 3/4: "+str(f2.reciprical()))
print("Reciprical of 7/8: "+str(f3.reciprical()))
print("-------------------------------------------------------------")
print("Reduces the object to its simpilest form and returns it")
print("15/20 Reduced to simpilest form: "+str(f1.simplify()))
print("3/4 Reduced to simpilest form: "+str(f2.simplify()))
print("7/8 Reduced to simpilest form: "+str(f3.simplify()))
print("-------------------------------------------------------------")
print("Takes in a fraction object and returns the decimal format of the fraction")
print("Decimal of 15/20: "+str(f1.decimal()))
print("Decimal of 3/4: "+str(f2.decimal()))
print("Decimal of 7/8: "+str(f3.decimal()))
print("-------------------------------------------------------------")
print("Takes a Fraction object and multiplies it by an integer")
print("15/20 multiplied by 3: "+str(f1.multiplyInt(3)))
print("3/4 multiplied by 8: "+str(f2.multiplyInt(8)))
print("7/8 multiplied by 2: "+str(f3.multiplyInt(2)))
print("15/20 multiplied by 11: "+str(f4.multiplyInt(11)))
print("-------------------------------------------------------------")
print("Overrides the addition sign, takes in 2 Fraction objects and returns the sum as a Fraction object")
print("f1(15/20)+f2(3/4) added: "+str(f1+f2))
print("f2(3/4)+f3(7/8) added: "+str(f2+f3))
print("f1(15/20)+f4(15/20) added: "+str(f1+f4))
print("-------------------------------------------------------------")
print("Overrides the multiply sign, takes in 2 Fraction objects and returns the product as a Fraction object")
print("f1(15/20)*f2(3/4) multiplied: "+str(f1*f2))
print("f2(3/4)*f3(7/8) multiplied: "+str(f2*f3))
print("f1(15/20)*f4(15/20) multiplied: "+str(f1*f4))
print("-------------------------------------------------------------")
print("Overrides the subtraction sign, takes in 2 Fraction objects and returns the difference as a Fraction object")
print("f1(15/20)-f2(3/4) subtracted: "+str(f1-f2))
print("f2(3/4)-f3(7/8) subtracted: "+str(f2-f3))
print("f1(15/20)-f4(15/20) subtracted: "+str(f1-f4))
print("-------------------------------------------------------------")
print("Overrides the division sign, takes in 2 Fraction objects and returns the quotient as a Fraction object")
print("f1(15/20)/f2(3/4) subtracted: "+str(f1/f2))
print("f2(3/4)/f3(7/8) subtracted: "+str(f2/f3))
print("f1(15/20)/f4(15/20) subtracted: "+str(f1/f4))
print("-------------------------------------------------------------")
print("Multiple Operations")
print("")
print("Example 1: f1(15/20)*f2(3/4)+f3(7/8)/f4(15/20)-f1(15/20),then decimal format")
print("Answer 1: "+str((f1*f2+f3/f4-f1).decimal()))
print("")
print("Example 2: f1(15/20)+f2(3/4)+f3(7/8)+f4(15/20), then simplified")
print("Answer 2: "+str((f1+f2+f3+f4).simplify()))
print("")
print("Example 3: f1(15/20)*f2(3/4)*f3(7/8)*f4(15/20),reduced,recipricalled")
print("Answer 3: "+str(((f1*f2*f3*f4).simplify()).reciprical()))