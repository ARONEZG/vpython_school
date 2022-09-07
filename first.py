from vpython import *


ball = sphere(pos=vector(0,1,0), color = color.red)
floor = box(pos=vector(0,0,50), size=vector(10,.2,100))
t = 0
dt = 0.01
vx = 1.5
vy = 4
g = 5
while True:
    rate(100)
    t = t + dt
    ball.pos.x = ball.pos.x + vx*t
    ball.pos.y = ball.pos.y + vy*t - (g * t * t)/2
