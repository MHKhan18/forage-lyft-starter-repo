from datetime import datetime

from car.car import Car
from engine.engine import Engine
from battery.battery import Battery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory:
    def create_calliope(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:

        engine: Engine = CapuletEngine(current_mileage, last_service_mileage)
        battery: Battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine: Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery: Battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(
        current_date: datetime, last_service_date: datetime, warning_light_on: bool
    ) -> Car:
        engine: Engine = SternmanEngine(warning_light_on)
        battery: Battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine: Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery: Battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine: Engine = CapuletEngine(current_mileage, last_service_mileage)
        battery: Battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
