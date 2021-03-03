# x = 1
# print ('sin(%g)=%g' % (x, sin(x)))

#The command does not know what sine is. You need to import the math.sin for it to work 

x = 1
from math import sin
print ('sin(%g)=%g' % (x, sin(x)))