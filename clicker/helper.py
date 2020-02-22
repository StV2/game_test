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
    obj.sprite = pygame.transform.rotate(obj.master_sprite, obj.rotation)
    obj.x = int(obj.center_x)
    obj.y = int(obj.center_y)

def check_events(type, list, event):
    for key in list:
        if key.type == type:
            event[key.type]()

def add_score(obj, value):
    pos = pygame.mouse.get_pos()
    rect = obj.sprite.get_rect()

    print(pos, rect.x, rect.y)
    if rect.collidepoint(pos):
        obj.vars["score"] += value
    else:
        print("missed")