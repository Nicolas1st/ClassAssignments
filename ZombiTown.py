from random import randint
from SunCloudStuff import *


class House:
    def __init__(self, latitude, longitude, number_of_doors):
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_doors = number_of_doors

    def zombie_is_nearby(self, doors, zombie, sunny):
        if (zombie.latitude - self.latitude) > 10 and (zombie.longitude - self.longitude) > 10 and sunny:
            for door in doors:
                door.open()


class Door:
    def __init__(self, name, state, hp=100, broken=False):
        self.id = name
        self.hp = hp
        self.state = state  # 1 - closed, 2 - open
        self.broken = broken

    def check_state(self):
        if self.hp > 0:
            self.broken = False
        else:
            self.broken = True

    def close(self):
        self.state = 1

    def open(self):
        self.state = 0

    def repair(self):
        self.hp += 10


class Zombie:
    def __init__(self, hp, power, latitude, longitude):
        self.hp = hp
        self.power = power
        self.latitude = latitude
        self.longitude = longitude

    def hit_door(self, door):
        door.hp -= self.power

    def heal(self):
        self.hp += 10

    def house_is_nearby(self, house):
        if house.latitude - self.latitude < 1:
            return True
        else:
            return False

    def search_for_house(self, house):
        if not self.house_is_nearby(house):
            self.latitude += randint(-10, 10)
        else:
            pass


