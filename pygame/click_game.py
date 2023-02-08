cry_man = Actor('no_cry_man')
cry_man.pos = 100, 100

WIDTH = 500
HEIGHT = 300
BACKGROUND_COLOR = (255,0,0)

def draw():
    screen.fill(BACKGROUND_COLOR)
    cry_man.draw()

def set_no_cry_man():
    cry_man.image = 'no_cry_man'

def set_cry_man():
    cry_man.image = 'cry_man'
    clock.schedule_unique(set_no_cry_man, 0.25)

def set_happy_man():
    cry_man.image = 'happy_man'
    clock.schedule_unique(set_no_cry_man, 1.0)

def update():
    cry_man.left = cry_man.left + 2
    if cry_man.left > WIDTH:
        cry_man.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_happy_man()
    else:
        set_cry_man()

