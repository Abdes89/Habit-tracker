from datetime import datetime
from typing import List, Optional
from db import get_connection
from models import Habit


def create_habit(user_id: int, title: str, description: str, periodicity: str) -> Habit:
    now = datetime.utcnow().isoformat()
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO habits (user_id, title, description, periodicity, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, title, description, periodicity, now))
        return Habit(cur.lastrowid, user_id, title, description, periodicity, datetime.fromisoformat(now))


def list_habits(user_id: int, include_archived=False) -> List[Habit]:
    with get_connection() as conn:
        cur = conn.cursor()
        sql = "SELECT * FROM habits WHERE user_id=?"
        if not include_archived:
            sql += " AND archived=0"
        cur.execute(sql, (user_id,))
        return [
            Habit(
                r["id"], r["user_id"], r["title"], r["description"],
                r["periodicity"], datetime.fromisoformat(r["created_at"]), bool(r["archived"])
            )
            for r in cur.fetchall()
        ]


def archive_habit(user_id: int, habit_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE habits SET archived=1 WHERE id=? AND user_id=?",
            (habit_id, user_id)
        )
        return cur.rowcount == 1


def log_completion(habit_id: int, when: Optional[datetime] = None):
    ts = (when or datetime.utcnow()).isoformat()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
            (habit_id, ts)
        )


def get_completions(habit_id: int) -> List[datetime]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT completed_at FROM completions WHERE habit_id=?",
            (habit_id,)
        ).fetchall()
        return [datetime.fromisoformat(r["completed_at"]) for r in rows]
