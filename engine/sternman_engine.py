from engine.engine import Engine
from dataclasses import dataclass


@dataclass
class SternmanEngine(Engine):

    warning_light_is_on: bool

    def needs_service(self) -> bool:
        return self.warning_light_is_on
