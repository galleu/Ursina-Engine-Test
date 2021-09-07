from math import fabs
from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
app.editor_ui_enabled = True

window.show_ursina_splash = True
window.borderless = False
window.title = "Test Game"
window.center_on_screen()

color.text_color = color.dark_text



for z in range(8):
    for x in range(8):
        pass
        
e = Entity(model='plane', texture='brick', position=(x,0,z), scale=(100,0,100), texture_scale=(100,100))



window.color=color.light_gray.tint(.1)
window.fps_counter.enabled = True
window.exit_button.visible = False

ec = EditorCamera(rotation_smoothing=2, enabled=1, rotation=(30,30,0))
player = FirstPersonController()
player.enabled = False

def input(key):
    if key == 'tab':
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled
    if key == 'c' or key == 'c hold':
        ec.position = (ec.position[0], ec.position[1] - 1, ec.position[2])
    if key == 'space' or key == 'space hold':
        ec.position = (ec.position[0], ec.position[1] + 1, ec.position[2])
    else:print(key)


app.run()