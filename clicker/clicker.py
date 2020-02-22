import pygame
from obj import Obj
from _collections import OrderedDict
import helper
pygame.init()

WIN_HEIGHT = 600
WIN_WIDTH = 800
BACKGROUND_COLOUR = (0, 0, 0)


display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
background.fill(BACKGROUND_COLOUR)

obj_surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

def clear_display():
    display.blit(background, (0, 0))
    obj_surf.fill((0, 0, 0))

def update_display():
    pygame.display.update()

def run_functions():
    for key in objects:
        for action in objects[key].actions:
            action()

def draw_objects():
    for key in objects:
        obj_surf.blit(objects[key].sprite, (objects[key].x, objects[key].y))

    display.blit(obj_surf, (0, 0))

objects = OrderedDict()
objects["background"] = Obj()
objects["cookie"] = Obj()

sprites = {
    "background": pygame.image.load("resources/background.jpg"),
    "cookie": pygame.image.load("resources/cookie.gif")
}

sprites["cookie"].set_colorkey((255, 255, 255))
sprites["background"] = pygame.transform.scale2x(sprites["background"])

objects["cookie"].sprite = sprites["cookie"]
objects["cookie"].x = int(WIN_WIDTH/2)
objects["cookie"].y = 300

objects["background"].sprite = sprites["background"]
objects["background"].x = int(WIN_WIDTH/2)
objects["background"].y = int(WIN_HEIGHT/2)

objects["background"].actions_push(lambda: helper.rotate(obj=objects["background"], amount=0.5))

END_FLAG = True

white = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
white.fill((255, 255, 255))

while END_FLAG:
    clear_display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            END_FLAG = False

    run_functions()

    print(objects["background"].x, objects["background"].x)

    draw_objects()

    update_display()

pygame.quit()