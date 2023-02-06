from math import sqrt

x1, y1 = 2,2
x2, y2 = 6,10

leg1 = abs(x1-x2)
leg2 = abs(y1-y2)

distance = sqrt(leg1 ** 2 + leg2 ** 2)

print (leg1)
print (leg2)
print ("Distance: " + str(distance))

slope = (y2-y1)/(x2-x1)

print ("Slope: " + str(slope))
