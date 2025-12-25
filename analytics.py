from datetime import date, timedelta
from functools import reduce
from typing import List, Tuple
from models import Habit


def _period_key(d: date, p: str) -> Tuple[int, int]:
    if p == "daily":
        return (d.year, d.timetuple().tm_yday)
    if p == "weekly":
        return d.isocalendar()[:2]
    return (d.year, d.month)


def _previous(key: Tuple[int, int], p: str):
    y, n = key
    if p == "daily":
        d = date(y, 1, 1) + timedelta(days=n - 1)
        return _period_key(d - timedelta(days=1), p)
    if p == "weekly":
        return (y, n - 1) if n > 1 else (y - 1, 52)
    return (y, n - 1) if n > 1 else (y - 1, 12)


def streak_length(dates: List[date], periodicity: str) -> int:
    if not dates:
        return 0
    periods = set(_period_key(d, periodicity) for d in dates)
    current = max(periods)

    def step(acc, _):
        key, count = acc
        prev = _previous(key, periodicity)
        return (prev, count + 1) if prev in periods else acc

    return reduce(step, range(len(periods)), (current, 1))[1]


def longest_streak(habits: List[Habit], completions: dict):
    scored = [
        (h.title, streak_length(completions[h.id], h.periodicity))
        for h in habits
    ]
    return max(scored, key=lambda x: x[1], default=None)
