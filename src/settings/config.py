NAME = "Pantheon"

WINDOW_SIZE = (800,600)

ARCHETYPTES = ["monotheism", "spiritualism", "paganism", "shamanism", "sectarianism", "cultism", "pantheon"]
REGIONS = [""]

TREE_MAX_SIZE = 100
PREDICATION_TREE = []
IDEOLOGY_TREE = []
INTERVENTIONS_TREE = []

# Passive gain of points per minutes
PASSIVE_GAIN = 1
# Inclusive range of points the player can gain by clicking on popups
RANGE_POINTS_GAIN = (1,4)
# The default speed of propagation of the atheism per minutes
ATHEISM_DEFAULT_SPEED = 1

# The events who's can randomly occurs
EVENTS = [["A problem has occured, how you wanna resolve it ?", ["Solution 1", 20, [["atheism", -5], ["beleivers", 900]]], ["Solution 2", 5, [["atheism", 10], ["beleivers", -500]]]]]

