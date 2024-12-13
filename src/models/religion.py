from src.models.tree import *

class Religion:
    def __init__(self, name:str, type:str, starting_point:str):
        self.name = name
        self.type = type
        self.beleivers = 0
        self.fanatics = 0
        self.enleighted = 0
        self.predication_1 = Tree(Node("Sanctuary", 50))
        self.predication_2 = Tree(Node("Missionary work", 50))
        self.ideology_1 = Tree(Node("Seminary", 50))
        self.ideology_2 = Tree(Node("Commendments", 50))
        self.intervention_1 = Tree(Node("Celestial messenger", 50))
        self.intervention_2 = Tree(Node("Theological discuss III", 50))
        self.locations = [starting_point]