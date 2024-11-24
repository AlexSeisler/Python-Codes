#1
def func(a):
    if a <6:
        return func(a+2)+a
    else:
        return (a-1)
print("#1. f(1)= "+str(func(1)))

#2
def func1(b):
    if b>=4:
        return func1(func1(b-2))+1
    elif b>=2 and b<4:
        return func1(b-1)-1
    elif b<2:
        return b+3
print("#2. f(9)= "+str(func1(9)))

#3
def func2(c,d):
    if c>6:
        return func2(c-2,2*d)+1
    elif c>2 and c<=6:
        return func2(c-3,d-1)+2
    elif c<=2:
        return c*2-d
print("#3. f(9,4)= "+str(func2(9,4)))

#4
def func3(e):
    if e>3:
        return func3(e-3)+3
    elif e==3:
        return e*2+1
    elif e<3:
        return e**2+2
print("#4. f(f(f(f(f(4)))))= "+str((func3(func3(func3(func3(func3(4))))))))

#5
def func5(f):
    if f>0 and f%2==0:
        return func5(f/2)-1
    elif f>0 and f%2==1:
        return func5(f-5)-2
    else:
        return f**2+3
print("#5. f(f(f(f(20))))= "+str(func5(func5(func5(func5(20))))))