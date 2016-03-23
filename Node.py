__author__ = 'edwingsantos'

import sys


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
        self.predecesor = None