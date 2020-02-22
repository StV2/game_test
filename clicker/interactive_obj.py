from obj import Obj
import helper
import pygame

class InteractiveObj(Obj):
    def __init__(self):
        super().__init__()

        self.__events = {}
        self.__listeners = {}
        self.vars = {
            "score": 0
        }
        self._actions = [lambda events: helper.check_events(pygame.MOUSEBUTTONDOWN, events, self.__events)]

    @property
    def listeners(self):
        return self.__listeners

    def add_listener(self, key, value):
        self.__listeners[key] = value

    @property
    def events(self):
        return self.__events

    def events(self, key, value):
        self.__events[key] = value