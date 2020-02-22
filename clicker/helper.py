import pygame

ALLOWABLE_TYPES = {
    "sprite": [pygame.Surface],
    "x": [int],
    "y": [int],
    "center_x": [int],
    "center_y": [int]
}

def rotate(obj, value):
    if obj.rotation >= 360:
        obj.rotation = 0
    else:
        obj.rotation += value
    print(obj.rotation)
    obj.sprite = pygame.transform.rotate(obj.master_sprite, obj.rotation)
    obj.x = int(obj.center_x)
    obj.y = int(obj.center_y)