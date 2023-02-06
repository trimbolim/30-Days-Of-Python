from math import sqrt

# y = x^2 + 6x + 9

for x in range(-10,10):
    y = x**2 + 6*x + 9
    print ("When x is: {0}, y is {1}".format(x,y))

a, b, c = 1,6,9

sol1 = (-b - sqrt(b**2 - 4*a*c))/(2 * a)
sol2 = (-b + sqrt(b**2 - 4*a*c))/(2 * a)

print ("solutions are {0} and {1}".format(sol1,sol2))

