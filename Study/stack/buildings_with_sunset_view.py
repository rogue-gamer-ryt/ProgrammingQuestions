"""
You are given a series of buildings that have windows facing west. The buildings are in a straight
line, and any building which is to the east of a building of equal or greater height cannot view the
sunset.

Design an algorithm that processes buildings in east-to-west order and returns the set of buildings
which view the sunset. Each building is specified by its height.
"""

# Time Complexity: O(n)
def examine_buildings_with_sunset(sequence):
    building_with_height = collections.namedtuple('BuildingWithHeight', ('id', 'height'))
    
    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(building_with_height(building_idx, building_height))
    
    return [candidate.id for candidate in reversed(candidates)]
