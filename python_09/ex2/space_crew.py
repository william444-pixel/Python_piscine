from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_safety(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        ranks = [m.rank for m in self.crew]
        if Rank.COMMANDER not in ranks and Rank.CAPTAIN not in ranks:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = \
                sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced_count < len(self.crew) / 2:
                raise ValueError("Long missions need at least 50% "
                                 "experienced crew (5+ years)")

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        crew = [
            CrewMember(member_id="C01", name="Sarah Connor",
                       rank=Rank.COMMANDER, age=40,
                       specialization="Mission Command", years_experience=15),
            CrewMember(member_id="C02", name="John Smith",
                       rank=Rank.LIEUTENANT, age=30,
                       specialization="Navigation", years_experience=6),
            CrewMember(member_id="C03", name="Alice Johnson",
                       rank=Rank.OFFICER, age=25,
                       specialization="Engineering", years_experience=2)
        ]

        valid_m = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_m.mission_name}")
        print(f"ID: {valid_m.mission_id}")
        print(f"Destination: {valid_m.destination}")
        print(f"Duration: {valid_m.duration_days} days")
        print(f"Budget: ${valid_m.budget_millions}M")
        print(f"Crew size: {len(valid_m.crew)}")
        print("Crew members:")
        for m in valid_m.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("=" * 41)
    print("Expected validation error:")

    try:
        invalid_crew = [
            CrewMember(member_id="C04", name="Bob No-Rank",
                       rank=Rank.CADET, age=20,
                       specialization="Cleaning", years_experience=0)
        ]
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Failing Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=invalid_crew,
            budget_millions=10.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
