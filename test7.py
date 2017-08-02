import math
def quadratic(a, b, c):
    x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x, y

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
x, y = quadratic(a, b, c)
print (x, y)
