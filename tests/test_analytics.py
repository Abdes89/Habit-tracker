from datetime import date
from analytics import streak_length

def test_daily():
    dates = [date(2025,1,1), date(2025,1,2), date(2025,1,3)]
    assert streak_length(dates, "daily") == 3

def test_weekly():
    dates = [date(2025,1,6), date(2025,1,13)]
    assert streak_length(dates, "weekly") == 2

def test_monthly():
    dates = [date(2025,1,10), date(2025,2,10), date(2025,3,10)]
    assert streak_length(dates, "monthly") == 3
