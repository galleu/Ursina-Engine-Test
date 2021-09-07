from ursina import *

ec = EditorCamera(rotation_smoothing=2, enabled=1, rotation=(30,30,0))

rotation_info = Text(position=window.top_left)

def update():
    rotation_info.text = str(int(ec.rotation_y)) + '\n' + str(int(ec.rotation_x))



#    if key == 'tab':    # press tab to toggle edit/play mode
#        ec.enabled = not ec.enabled
#        player.enabled = not player.enabled
