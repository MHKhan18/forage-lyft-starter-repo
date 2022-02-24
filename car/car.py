from dataclasses import dataclass

from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery


@dataclass
class Car(Serviceable):

    engine: Engine
    battery: Battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
