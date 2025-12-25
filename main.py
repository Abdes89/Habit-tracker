import questionary
from services_users import register_user, login_user
from services_habits import (
    create_habit, list_habits, archive_habit,
    log_completion, get_completions
)
from analytics import streak_length
from db import init_db


def main():
    init_db()
    user = None

    while True:
        if not user:
            choice = questionary.select(
                "Welcome",
                ["Register", "Login", "Exit"]
            ).ask()

            if choice == "Register":
                user = register_user(
                    questionary.text("Username").ask(),
                    questionary.password("Password").ask()
                )
            elif choice == "Login":
                u = login_user(
                    questionary.text("Username").ask(),
                    questionary.password("Password").ask()
                )
                if u:
                    user = u
                else:
                    questionary.print("Login failed")
            else:
                break

        else:
            choice = questionary.select(
                f"Main Menu ({user.username})",
                ["Create Habit", "List Habits", "Log Completion", "Archive Habit", "Analytics", "Logout"]
            ).ask()

            if choice == "Create Habit":
                create_habit(
                    user.id,
                    questionary.text("Title").ask(),
                    questionary.text("Description").ask(),
                    questionary.select("Periodicity", ["daily", "weekly", "monthly"]).ask()
                )

            elif choice == "List Habits":
                for h in list_habits(user.id, True):
                    questionary.print(f"{h.id} | {h.title} | {h.periodicity} | archived={h.archived}")

            elif choice == "Log Completion":
                hid = int(questionary.text("Habit ID").ask())
                log_completion(hid)

            elif choice == "Archive Habit":
                hid = int(questionary.text("Habit ID").ask())
                archive_habit(user.id, hid)

            elif choice == "Analytics":
                for h in list_habits(user.id):
                    dates = [d.date() for d in get_completions(h.id)]
                    s = streak_length(dates, h.periodicity)
                    questionary.print(f"{h.title}: {s}")

            else:
                user = None


if __name__ == "__main__":
    main()
