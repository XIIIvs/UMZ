import pyglet
from pyglet.window import key
from pyglet.window import mouse

print("http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html")

window = pyglet.window.Window()

label = pyglet.text.Label('EXERCISES',
                          font_name='Arial',
                          font_size=13,
                          x=window.width//2,
                          y=window.height//2,
                          anchor_x='center',
                          anchor_y='center'
)

image = pyglet.resource.image('tst.jpg')

@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(10, 10)

@window.event
def on_key_press(symbol, modifiers):
    print('Key pressed', symbol, modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
    print("Mouse", x, y, button, modifiers)

if __name__ == "__main__":
    pyglet.app.run()