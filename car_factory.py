from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_sensors)
        return Car(engine, battery, tires)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_sensors)
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_sensors):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_sensors)
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_sensors)
        return Car(engine, battery, tires)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_sensors)
        return Car(engine, battery, tires)
        