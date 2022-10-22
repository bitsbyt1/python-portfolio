
from turtle import *
state = {'turn': 0}

def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, '#00b4d8')
    back(100)
    right(120)
    forward(100)
    dot(120, '#caf0f8')
    back(100)
    right(120)
    forward(100)
    dot(120, '#023e8a')
    back(100)
    right(120)
    update()


def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 5)

def flick():
    state['turn']+=10

setup(400, 400, 400, 0)
hideturtle()
tracer(False)
width(30)
onkey(flick, 'space')
listen()
animate()
done()
 
