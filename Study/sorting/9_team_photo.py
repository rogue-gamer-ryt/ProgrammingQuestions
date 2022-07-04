"""
Design an algorithm that takes as input two teams and the heights of the players in the teams and
checks if it is possible to place players to take the photo subject to the placement constraint.
"""
# TIme - O(nlogn)
class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks if A can be placed in front of B
    @staticmethod
    def valid_placement_exists(A, B):
        return all(a < b for a, b in zip(sorted(A._players), sorted(B._players)))