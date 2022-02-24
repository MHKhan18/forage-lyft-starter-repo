from battery.battery import Battery
from dataclasses import dataclass
from datetime import datetime


@dataclass
class NubbinBattery(Battery):

    last_service_date: datetime
    current_date: datetime

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4
        )
        return service_threshold_date < datetime.today().date()
