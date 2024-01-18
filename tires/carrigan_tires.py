from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for value in self.sensors:
            if value >= 0.9:
                return True
        return False