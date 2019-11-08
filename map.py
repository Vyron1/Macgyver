#############
#  Imports  #
#############
import pygame as pg
from settings import *

class Map:

    def __init__(self):
        self.treated_map = 0


    def generate(self):
        with open("map.txt", "r") as map:
            treated_map = []
            for line in map:
                map_line = []
                for ch in line:
                    if ch != "\n":
                        map_line.append(ch)
                treated_map.append(map_line)
            self.treated_map = treated_map

    def show_map(self, window):
        wall = pg.image.load(image_wall).convert()
        floor = pg.image.load(image_floor).convert()
        start = pg.image.load(image_start).convert()
        finish = pg.image.load(image_finish).convert()
        guard = pg.image.load(image_guard).convert_alpha()
        object_1 = pg.image.load(image_object_1).convert_alpha()
        object_2 = pg.image.load(image_object_2).convert_alpha()
        object_3 = pg.image.load(image_object_3).convert_alpha()
        numb_line = 0
        for line in self.treated_map:
            numb_ch = 0
            for ch in line:
                x = numb_ch * size_sprite
                y = numb_line * size_sprite
                if ch == "#":
                    window.blit(wall, (x, y))
                elif ch == " ":
                    window.blit(floor, (x, y))
                elif ch == "s":
                    window.blit(start, (x, y))
                elif ch == "f":
                    window.blit(finish, (x, y))
                    window.blit(guard, (x, y))
                elif ch == "1":
                    window.blit(floor, (x, y))
                    window.blit(object_1, (x, y))
                elif ch == "2":
                    window.blit(floor, (x, y))
                    window.blit(object_2, (x, y))
                elif ch == "3":
                    window.blit(floor, (x, y))
                    window.blit(object_3, (x, y))

                numb_ch += 1
            numb_line += 1