from enum import StrEnum
from pydantic import BaseModel, Field, computed_field


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"
    ALL = "all"


class Income(StrEnum):
    ABC = "ABC"
    AC = "AC"
    BC = "BC"
    B = "B"
    C = "C"


class GeneticsMode(StrEnum):
    QUICK = "quick"
    DEEP = "deep"


class AudienceReach(BaseModel):
    age_from: int = Field(ge=0)
    age_to: int = Field(ge=0)
    percentage: float = Field(ge=0, le=100)


class Part1Response(BaseModel):
    value: float = Field(ge=0, le=100)
    reach: list[AudienceReach]


class TargetAudience(BaseModel):
    age_from: int = Field(ge=0)
    age_to: int = Field(ge=0)
    gender: Gender
    income: Income

    @property
    def TA(self) -> dict[str, ...]:
        return {
            "gender": self.gender,
            "ageFrom": self.age_from,
            "ageTo": self.age_to,
            "income": self.income.lower()
        }


class Coordinates(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class Polygon(BaseModel):
    top_left: Coordinates
    bottom_right: Coordinates
    count: int = Field(gt=0)
    title: str = None

    @computed_field
    @property
    def center(self) -> Coordinates:
        return Coordinates(
            latitude=(self.top_left.latitude + self.bottom_right.latitude) / 2,
            longitude=(self.top_left.longitude + self.bottom_right.longitude) / 2,
        )

    @computed_field
    @property
    def polygon(self) -> list[list[float]]:
        return [
            [self.top_left.latitude, self.top_left.longitude],
            [self.top_left.latitude, self.bottom_right.longitude],
            [self.bottom_right.latitude, self.bottom_right.longitude],
            [self.bottom_right.latitude, self.top_left.longitude]
        ]
