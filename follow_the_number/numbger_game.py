WIDTH = 400
HEIGHT = 400
import random

dots = []

lines = []

next_dot = 0

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    print(dots)
    print(lines)
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), dot.pos[0], dot.pos[1] + 12)
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line., line.y, (100, 0, 0))
