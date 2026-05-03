from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    witness_count: int = Field(ge=1, le=100)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    is_verified: bool = False
    message_received: str | None = Field(default=None, max_length=200)

    @model_validator(mode="after")
    def validation(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('contact_id must start with "AC"')
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified!")

        if self.contact_type == ContactType.telepathic \
                and self.witness_count <= 3:
            raise ValueError("Telepathic contact requires"
                             "more than 3 witnesses")

        if self.signal_strength > 7.0:
            print("Signal strength is very high!")
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 40)
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            witness_count=5,
            signal_strength=8.5,
            duration_minutes=45,
            message_received="Greetings from Zeta Reticuli")
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Witnesses: {contact.message_received}")
    except ValueError as e:
        print(e)
    print("=" * 40)
    print("Expected validation error:")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            witness_count=1,
            signal_strength=8.5,
            duration_minutes=45,
            message_received="Greetings from Zeta Reticuli")
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Witnesses: {contact.message_received}")
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
