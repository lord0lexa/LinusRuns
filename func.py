import pygame, random, sys

def floor_moving(floor_a, floor_b, velocity):
    floor_a -= velocity
    floor_b -= velocity

    if floor_a < -1240:
        floor_a = 1240

    if floor_b < -1240:
        floor_b = 1240

    return floor_a, floor_b

def scene_moving(x, velocity):
    x -= velocity
    if x < -1250:
        x = 1250

    return x