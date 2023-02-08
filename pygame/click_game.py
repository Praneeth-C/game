cry_man = Actor('no_cry_man')
cry_man.pos = 100, 100

WIDTH = 500
HEIGHT = 300
BACKGROUND_COLOR = (255,0,0)

def draw():
    screen.fill(BACKGROUND_COLOR)
    cry_man.draw()

def update():
    cry_man.left = cry_man.left + 2
    if cry_man.left > WIDTH:
        cry_man.right = 0
