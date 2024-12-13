from src.models.wallet import *
from src.models.tree import *
from settings.config import *

class AbilitiesTree :
    def __init__(self, name:str, content:list):
        pass
    def copy_content(self, list_content:list):
        limit = TREE_MAX_SIZE
        looper = True
        reader = list_content
        tree = Tree(Node(list_content[0], list_content[1]))
        while ((looper == True) or (limit == 0)):
            if (reader == []):
                looper = False
            else :
                if (len(reader) > 4):
                    pass


abr = ["root", ["enfant 1", ["petit enfant 1"]], ["enfant 2", ["petit enfant 2", ["arriere petit enfant 1"]]]]