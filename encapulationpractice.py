class Car():
    def __init__(self, topspeed, weight, acceleration_rate):
        self.top_speed = topspeed
        self.current_speed = 0
        self.weight = weight
        self.acceleration_rate = acceleration_rate

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, new_current_speed):
        if new_current_speed >= 0:
            if new_current_speed > self.top_speed:
                self._current_speed = self.top_speed
            else:
                self._current_speed = new_current_speed
        else:
            self._current_speed = 0

    @property
    def top_speed(self):
        return self._top_speed

    @top_speed.setter
    def top_speed(self, new_top_speed):
        if new_top_speed >= 0:
            self._top_speed = new_top_speed
        else:
            self._top_speed = 0

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight >= 0:
            self._weight = new_weight
        else:
            self._weight = 0

    @property
    def acceleration_rate(self):
        return self._acceleration_rate

    @acceleration_rate.setter
    def acceleration_rate(self, new_acceleration_rate):
        if new_acceleration_rate >= 0:
            self._acceleration_rate = new_acceleration_rate
        else:
            self._acceleration_rate = 0

    def accelerate(self):
        self.current_speed += self.acceleration_rate

    def brake(self):
        self.current_speed = 0


my_car = Car(40, 20, 10)

print(f"current speed: {my_car.current_speed}")
print(f"top speed: {my_car.top_speed}")
print(f"weight: {my_car.weight}")
print(f"acceleration rate: {my_car.acceleration_rate}")
my_car.accelerate()
print(f"current speed: {my_car.current_speed}")
my_car.accelerate()
print(f"current speed: {my_car.current_speed}")
my_car.accelerate()
print(f"current speed: {my_car.current_speed}")
my_car.accelerate()
print(f"current speed: {my_car.current_speed}")
my_car.accelerate()
print(f"current speed: {my_car.current_speed}")
my_car.brake()
print(f"current speed: {my_car.current_speed}")

        

