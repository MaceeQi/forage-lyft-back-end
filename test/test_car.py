import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

# from engine.model.calliope import Calliope
# from engine.model.glissade import Glissade
# from engine.model.palindrome import Palindrome
# from engine.model.rorschach import Rorschach
# from engine.model.thovex import Thovex


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_be_serviced2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 40)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_be_serviced2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 30)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced1(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced2(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced1(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_be_serviced2(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced1(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_should_not_be_serviced2(self):
        current_mileage = 3000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced1(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_be_serviced2(self):
        current_mileage = 120000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced1(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_should_not_be_serviced2(self):
        current_mileage = 6000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced1(self):
        sensors = [0.9, 0, 0, 0]

        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_be_serviced2(self):
        sensors = [0.89, 0.89, 0.91, 0.899]

        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_be_serviced3(self):
        sensors = [0, 0.99, 1, 0]

        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced1(self):
        sensors = [0.89, 0.89, 0.89, 0.89]

        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())

    def test_tires_should_not_be_serviced2(self):
        sensors = [0.89, 0, 0.5, 0.09]

        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())

    def test_tires_should_not_be_serviced3(self):
        sensors = [0, 0, 0, 0]

        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced1(self):
        sensors = [1, 1, 1, 0]

        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_be_serviced2(self):
        sensors = [1, 1, 0.9, 0.1]

        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_be_serviced3(self):
        sensors = [0.9, 0.9, 0.99, 0.5]

        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced1(self):
        sensors = [1, 1, 0.99, 0]

        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())

    def test_tires_should_not_be_serviced2(self):
        sensors = [0, 0, 0.99, 1]

        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())

    def test_tires_should_not_be_serviced3(self):
        sensors = [0, 0, 0, 0]

        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())


# class TestCalliope(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
