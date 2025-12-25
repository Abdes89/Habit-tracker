import hashlib
from datetime import datetime
from typing import Optional
from db import get_connection
from models import User


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username: str, password: str) -> User:
    now = datetime.utcnow().isoformat()
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
            (username, _hash(password), now)
        )
        return User(cur.lastrowid, username, datetime.fromisoformat(now))


def login_user(username: str, password: str) -> Optional[User]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        if not row or row["password_hash"] != _hash(password):
            return None
        return User(row["id"], row["username"], datetime.fromisoformat(row["created_at"]))
