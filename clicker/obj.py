from decorators import *

class Obj:
    def __init__(self):
        self.__spr = None
        self.__master_spr = None
        self.__x = None
        self.__y = None
        self.__rotation = 0
        self.__actions = []

    @property
    def sprite(self):
        if self.__spr is not None:
            return self.__master_spr
        else:
            raise ReferenceError("There is no sprite added to this object")

    @sprite.setter
    @typechecked
    def sprite(self, value):
        if self.__spr is None:
            self.__master_spr = value
        self.__spr = value

    @property
    def x(self):
        if self.__x is not None:
            return self.__x - int(self.__spr.get_width() / 2)
        else:
            raise ReferenceError("There is no x coord assigned to this object")

    @x.setter
    @typechecked
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        if self.__y is not None:
            return self.__y - int(self.__spr.get_height() / 2)
        else:
            raise ReferenceError("There is no y coord assigned to this object")

    @y.setter
    @typechecked
    def y(self, value):
        self.__y = value

    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, value):
        self.__actions = value

    def actions_pop(self):
        return self.__actions.pop()

    def actions_push(self, value):
        self.__actions.append(value)

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value

    @property
    def master_sprite(self):
        return self.__master_spr.copy()