from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid_station = SpaceStation(
                station_id="ISS-01",
                name="International Space Station",
                crew_size=6,
                power_level=95.5,
                oxygen_level=98.0,
                last_maintenance="2026-04-27T12:00:00")
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print("Status:"
              f"{'Operational' if valid_station.is_operational else 'Down'}\n")
    except ValidationError as e:
        print(f"Validation Error:\n{e}")
    print("=" * 40)
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print("Valid station created:")
        print(f"ID: {invalid_station.station_id}")
        print(f"Name: {invalid_station.name}")
        print(f"Crew: {invalid_station.crew_size} people")
        print(f"Power: {invalid_station.power_level}%")
        print(f"Oxygen: {invalid_station.oxygen_level}%")
        print("Status:"
              f"{'Operational' if invalid_station.is_operational else 'Down'}")
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
