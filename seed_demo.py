from services_users import register_user, login_user
from services_habits import create_habit, log_completion
from db import init_db
from datetime import datetime, timedelta
import random


def seed():
    init_db()
    try:
        user = register_user("demo", "demo123")
    except:
        user = login_user("demo", "demo123")

    habits = [
        ("Inbox Triage", "Process incoming messages", "daily"),
        ("Update Project Notes", "Write daily notes", "daily"),
        ("Workspace Reset", "Reset workspace", "daily"),
        ("Weekly Planning", "Plan next week", "weekly"),
        ("Document Filing", "Organize documents", "weekly"),
        ("Cleanup Downloads", "Clean downloads folder", "monthly"),
        ("Personal Admin Day", "Handle admin tasks", "monthly"),
    ]

    for h in habits:
        try:
            create_habit(user.id, *h)
        except:
            pass

    for i in range(28):
        day = datetime.utcnow() - timedelta(days=i)
        for hid in range(1, 8):
            if random.random() > 0.4:
                log_completion(hid, day)


if __name__ == "__main__":
    seed()
