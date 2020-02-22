import pygame

ALLOWABLE_TYPES = {
    "sprite": [pygame.Surface],
    "x": [int],
    "y": [int]
}

def rotate(obj, amount):
    if obj.rotation >= 360:
        obj.rotation = 0
    else:
        obj.rotation += amount
    obj.sprite = pygame.transform.rotate(obj.master_sprite, obj.rotation)