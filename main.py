from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

window.fullscreen = True
window.color = color.cyan
window.title = "Minecraft"
window.always_on_top = True
window.borderless = True
window.position = [0, 0]
window.editor_ui.enabled = False
window.exit_button.visible = False
window.icon = "icon.ico"

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        if position[1] == 0:
            colorVoxel = color.rgb32(0, random.randint(100, 255), 0)
        elif position[1] == -8:
            colorVoxel = color.rgb32(0, 0, 0)
        elif position[1] < 0 and position[1] > -3:
            colorVoxel = color.rgb32(random.randint(50, 100), random.randint(50, 100), 0)
        else:
            rand = random.randint(50, 150)
            colorVoxel = color.rgb32(rand, rand, rand)

        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=colorVoxel,
            highlight_color=color.white,
        )

for z in range(-8, 8):
    for x in range(-8, 8):
        for y in range(0, -9, -1):
            voxel = Voxel(position=(x, y ,z))


def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
        
            Sequence(
                Func(hand.animate_position, (0.5, -0.3), duration=0.1),
                Wait(0.25),
                Func(hand.animate_position, (0.6, -0.5), duration=0.1)
            ).start()
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

        Sequence(
            Func(hand.animate_position, (0.5, -0.3), duration=0.1),
            Wait(0.25),
            Func(hand.animate_position, (0.6, -0.5), duration=0.1)
        ).start()
    if key == 'f3':
        window.editor_ui.enabled = not window.editor_ui.enabled


hand = Entity(
    parent=camera.ui,
    model='quad',
    texture='white_cube',
    color=color.rgb32(255, 220, 180),
    scale=(0.23, 0.6),
    position=(0.6, -0.5),
    rotation=(0, 0, -25)
)


player = FirstPersonController()
app.run()
