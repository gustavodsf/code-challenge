'''
An ant on the floor can move in the 4 diagonal directions, which are defined from the point of view of a fixed aerial observer (the ant does not "turn").

You are given the parameter moves, an array of integers, containing the ant steps. Calculate the Euclidean distance between the starting position and the final position of the ant.

Each step is a value between 0 and 3:

- 0: the ant moves one unit to the up and one unit to the right.
- 1: the ant moves one unit to the down and one unit to the right.
- 2: the ant moves one unit to the down and one unit to the left.
- 3: the ant moves one unit to the up and one unit to the left.
'''
from json import dumps, loads
from typing import List
from math import sqrt


def compute_distance(moves: List[int]) -> int:
    x = 0
    y = 0
    for move in moves:
        if move == 0:
            x +=1
            y +=1
        elif move == 1:
            y-=1
            x+=1
        elif move == 2:
            x-=1
            y-=1
        elif move == 3:
            x-=1
            y+=1
    distance = sqrt(x**2 + y**2)
    return int(distance)
