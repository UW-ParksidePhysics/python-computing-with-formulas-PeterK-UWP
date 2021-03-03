from math import pi
C_d = 0.2 #drag of air
p = 1.2 # kgm^-3 desnity of air
a = 0.11 #meters radius
A = pi*a**2 #area in meters squared
m = 0.43 # kg mass
V1 = 33.33 #velocity m/s Hard kick
V2 = 2.78 #velocity in m/s soft kick
g = 9.8 # gravity
Fg = m*g  #force due to gravity
Fd1 = 0.5*C_d*p*A*V1**2
Fd2 = 0.5*C_d*p*A*V2**2
print(Fd1)
print(Fd2)
print(Fg)
print(Fd1/Fg)
print(Fd2/Fg)