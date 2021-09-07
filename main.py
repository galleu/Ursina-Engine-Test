from ursina import *
import time
import _thread

app = Ursina(vsync=False)


class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)




for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x,0,z))

Cursor()


from player import player
from update import update


def StartJump():
    print("Starting Jump")
    time.sleep(5)
    player.main.log = True
    print("Log True")


def input(key):
    print(key)
    if key == "escape":
        quit()
    if key == "tab":
        _thread.start_new_thread(StartJump, ())
        print(player.main.jump())





app.run()