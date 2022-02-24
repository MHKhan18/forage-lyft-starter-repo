from engine.engine import Engine
from dataclasses import dataclass


@dataclass
class WilloughbyEngine(Engine):

    current_mileage: int
    last_service_mileage: int

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
