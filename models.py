
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

Periodicity = Literal["daily", "weekly", "monthly"]


@dataclass(frozen=True)
class User:
    id: int
    username: str
    created_at: datetime


@dataclass(frozen=True)
class Habit:
    id: int
    user_id: int
    title: str
    description: str
    periodicity: Periodicity
    created_at: datetime
    archived: bool = False
