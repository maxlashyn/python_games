from options import *
from random import randint
from math import sqrt

def get_random_pos():
    return randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT)


def get_distance(start_pos, end_pos):
    return int(sqrt((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2))
