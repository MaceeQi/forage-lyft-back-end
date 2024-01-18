from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sensors_sum = 0
        for value in self.sensors:
            sensors_sum += value

        return sensors_sum >= 3