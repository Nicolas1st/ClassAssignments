import math


class Sun:
    def __init__(self, zenit_height, angle, day_length):
        self.zenit_height = zenit_height
        self.angle = angle  # specified in radians
        self.position = zenit_height * math.cos(angle)
        self.cur_height = zenit_height * math.sin(angle)
        self.day_length = day_length

    def move(self, time_period):
        progression_rate = math.pi/2 / self.day_length
        self.angle += progression_rate

    def casted_shadow(self, cloud):
        if self.cur_height <= cloud.height:
            return self.zenit_height + 1, self.zenit_height + 2  # no shadow, or it is beyond Earth
        elif self.cur_height > cloud.height:
            k = self.cur_height / (self.cur_height - cloud.height)
            if self.position == cloud.position:
                shadow_lbound = cloud.position - cloud.width / 2 * k
                shadow_rbound = cloud.position + cloud.width/2 * k
                return shadow_lbound, shadow_rbound
            elif self.position > cloud.position:
                center_displacement = self.position - cloud.position
                shadow_lbound = center_displacement - cloud.width / 2 * k
                shadow_rbound = center_displacement + cloud.width / 2 * k
                return shadow_lbound, shadow_rbound
            elif self.position < cloud.position:
                center_displacement = cloud.position - self.position
                shadow_lbound = center_displacement - cloud.width / 2 * k
                shadow_rbound = center_displacement + cloud.width / 2 * k
                return shadow_lbound, shadow_rbound


class Cloud:
    def __init__(self, height, width, position, velocity):
        self.height = height
        self.width = width
        self.position = position
        self.velocity = velocity

    def move(self, time_period):
        self.position += self.velocity * time_period


class LightDetector:
    def __init__(self, position):
        self.position = position

    def is_sunny(self, sun, cloud):
        shadow_lbound, shadow_rbound = sun.casted_shadow(cloud)
        if shadow_lbound <= self.position <= shadow_rbound:
            return False
        else:
            return True


sun = Sun(100, math.pi/2, 12)  # height, angle, day_length
cloud = Cloud(60, 10, -50, 10)  # height, width, position, velocity
sensor = LightDetector(0)
for i in range(100):
    sun.move(1)
    cloud.move(10)
    print(sensor.is_sunny(sun, cloud))