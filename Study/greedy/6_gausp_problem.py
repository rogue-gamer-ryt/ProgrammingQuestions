"""
In the gasup problem, a number of cities are arranged on a circular road. You need to visit all the
cities and come back to the starting city. A certain amount of gas is available at each city. The
amount of gas summed up over all cities is equal to the amount of gas required to go around the
road once. Your gas tank has unlimiled capacity. Call a city arnple if you can begin at that city with
an empty tank, refill at it, then travel through all the remaining cities, refilling at each, and retum
to the ample city, without running out of gas at any point.
Given an instance of the gasup problem, how would you efficiently compute an ample city? You
can assume that there exists an ample city.
"""

MPG = 20
def find_ample_city(gallons, distances):
    remaining_gallons = 0
    CityAndRemaningGas = collections.namedtuple('CityAndRemaningGas', ('city', 'remaining_gallons'))

    city_remaining_gallons_pair = CityAndRemaningGas(0,0)
    num_cities = len(gallons)

    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)
    return city_remaining_gallons_pair.city