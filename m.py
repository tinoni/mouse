from pynput.mouse import Button, Controller
from random import randrange
import time

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
#mouse.position = (10, 20)
#print('Now we have moved it to {0}'.format(
    #mouse.position))

# Move pointer relative to current position
while True:
    h = randrange(-1, 1)
    v = randrange(-1, 1)
    mouse.move(h, v)
    print('Now we have moved it to {0}'.format(mouse.position))
    time.sleep(10)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
#mouse.click(Button.left, 2)

# Scroll two steps down
#mouse.scroll(0, 2)
