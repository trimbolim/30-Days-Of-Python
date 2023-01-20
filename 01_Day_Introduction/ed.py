import math

p1x = 2
p1y = 3
p2x = 10
p2y = 8

leg1 = abs(p1x - p2x)
leg2 = abs(p1y - p2y)

print ("leg 1: " + str(leg1))
print ("leg 2: " + str(leg2))

squared_legs_sum = leg1 ** 2 + leg2 ** 2

eu_distance = math.sqrt(squared_legs_sum)

print ("Euq dist: " + str(eu_distance))

# Foo