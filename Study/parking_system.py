class Vehicle:
    def __init__(self, spot_size):
        self._spot_size = spot_size
    
    def get_spot_size(self):
        return self._spot_size

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)

class SemiTruck(Vehicle):
    def __init__(self):
        super().__init__(3)


class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0
    
    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def charge(self, amount):
        self._payment_due += amount

class ParkingFloor:
    def __init__(self, spot_count):
        self._spots = [0] * spot_count
        self._vehicle_map = {}

    def park_vehicle(self, vehicle):
        """Park a vehicle on the nearest available spot range"""
        size = vehicle.get_size()

        l, r = 0, 0
        while r < (self._spots):
            if self._spots[r] != 0:
                l = r + 1
            if r - l + 1 == size:
                # Park the vehicle when you find a range of spots empty
                for k in range(l, r = 1):
                    self._spots[k] = 1
                self._vehicle_map[vehicle] = [l, r]

                return True
            r += 1
        
        return False
    
    def remove_vehicle(self, vehicle):
        """Remove a vehicle from a parked spot"""
        l, r = self._vehicle_map[vehicle]
        for k in range(l, r + 1):
            self._spots[k] = 0
        del self._vehicle_map[vehicle]
        # charge driver?
    
    def get_parking_spots(self):
        return self._spots

    def get_vehicle_spots(self, vehicle):
        return self._vehicle_map.get(vehicle)
    
class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor):
        self._floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle):
        for floor in self._floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle):
        for floor in self._floors:

            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False
    
class ParkingSystem:
    def __init__(self, parking_garage, hourly_rate):
        self._parking_garage = parking_garage
        self._hourly_rate = hourly_rate
        self._time_parked = {}

    def park_vehicle(self, driver):
        current_hour = datetime.datetime.now()
        is_parked = self._parking_garage.park_vechile(driver.get_vehicle())
        if is_parked:
            self._time_parked[driver.get_id()] = current_hour
        return is_parked

    def remove_vehicle(self, driver):
        if driver.get_id() not in self._time_parked:
            return False
        
        current_hour = datetime.datetime.now()
        time_parked = math.ceil(current_hour - self._time_parked[driver.get_id()])
        driver.charge(time_parked * self._hourly_rate)

        del self._time_parked[driver.get_id()]
        return self._parking_garage.remove_vehicle(self.driver.get_vehicle())
