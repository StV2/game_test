from decorators import *

class Obj:
    def __init__(self):
        self.__spr = None
        self.__master_spr = None
        self.__x = None
        self.__center_x = None
        self.__y = None
        self.__center_y = None
        self.__rotation = 0
        self.__actions = []

    @property
    def sprite(self):
        if self.__spr is not None:
            return self.__spr
        else:
            raise ReferenceError("There is no sprite added to this object")

    @sprite.setter
    @typechecked
    def sprite(self, value):
        if self.__spr is None:
            self.__master_spr = value.copy()

        print("setting_sprite")
        self.__spr = value

    @property
    def x(self):
        if self.__x is not None:
            return self.__x
        else:
            raise ReferenceError("There is no x coord assigned to this object")

    @x.setter
    @typechecked
    def x(self, value):
        offset = int(self.__spr.get_width() / 2)
        self.__x = value - offset

    @property
    def y(self):
        if self.__y is not None:
            return self.__y
        else:
            raise ReferenceError("There is no y coord assigned to this object")

    @y.setter
    @typechecked
    def y(self, value):
        offset = int(self.__spr.get_height() / 2)
        self.__y = value - offset

    @property
    def center_x(self):
        if self.__center_x is not None:
            return self.__center_x
        else:
            raise ReferenceError("There is no center_x coord assigned to this object")

    @center_x.setter
    @typechecked
    def center_x(self, value):
        self.__center_x = value

    @property
    def center_y(self):
        if self.__center_y is not None:
            return self.__center_y
        else:
            raise ReferenceError("There is no center_y coord assigned to this object")

    @center_y.setter
    @typechecked
    def center_y(self, value):
        self.__center_y = value

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
        return self.__master_spr