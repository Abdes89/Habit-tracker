# Project Hygiene Habit Tracker (CLI)

The **Project Hygiene Habit Tracker** is a Python-based command-line application that helps users track  
**organizational and project-related habits** (project hygiene), such as planning, documentation, and administrative routines.  
It is intentionally not focused on fitness or health, but on maintaining reliable habits that support structured project work.

This project was developed for  
**DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python**.

---

## Table of Contents
- Features
- Architecture Overview
- Storage & Data Flow
- Installation
- Usage (CLI Workflow)
- Fixtures & Demo Data (Assignment Requirement)
- Testing
- Project Structure
- Challenges & Solutions
- Future Improvements

---

## Features

### User Management
- User registration and login
- Passwords stored as hashes
- One active user per CLI session

### Habit Management
- Create habits with fixed periodicity: **daily**, **weekly**, **monthly**
- List active and archived habits
- Archive habits instead of deleting them (history is preserved)
- Log habit completions

### Analytics
- Display streaks per habit
- Determine the longest streak across all habits
- Period-aware streak logic:
  - Daily → calendar day
  - Weekly → ISO calendar week
  - Monthly → calendar month

### Interface
- Menu-driven CLI using **questionary**
- Clear workflow: *Create → Check-off → View analytics*

---

## Architecture Overview

The application follows a **layered, modular architecture**:

- **models.py** – domain entities (`User`, `Habit`)
- **services_users.py** – user registration and authentication
- **services_habits.py** – habit management and completion logging
- **analytics.py** – pure analytical functions (functional style)
- **db.py** – SQLite initialization and connection handling
- **main.py** – CLI orchestration and user interaction

---

## Storage & Data Flow (SQLite)

Persistent storage is implemented using **SQLite**.

### Tables
- `users`
- `habits`
- `completions`

### Data Flow
1. CLI triggers an action
2. Service layer reads/writes via `db.py`
3. Analytics operate on retrieved data (no streak values stored)

---

## Installation

bash
git clone <your-repository-url>
cd project-hygiene-habit-tracker

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python db.py
`

---

## Usage (CLI Workflow)

bash
python main.py


Typical workflow:

1. Register or log in
2. Create habits
3. Log completions
4. View analytics
5. Archive habits

---

## Fixtures & Demo Data (Assignment Requirement)

The assignment requires **at least five predefined habits** and **four weeks of data**.

This project provides **seven predefined habits**, of which:

* **Five are assignment fixtures**
* **Two are optional extensions**

Generate demo data:

bash
python seed_demo.py


---

## Testing

bash
python db.py
python seed_demo.py
pytest


Tests focus on:

* Daily, weekly, and monthly streak logic
* Correctness of analytics functions

---

## Project Structure

text
project-hygiene-habit-tracker/

 
├── analytics.py

├── db.py

├── main.py

├── models.py

├── requirements.txt

├── seed_demo.py

├── services_habits.py

├── services_users.py

└── tests/

        └── test_analytics.py


---

## Challenges & Solutions

* Handling streak calculations across calendar boundaries
* Preserving historical data via archiving instead of deletion

---

## Future Improvements

* GUI or web-based frontend
* Notification features
* Extended analytics



## CLI Implementation Note

The command-line interface is implemented using the *questionary* library, which provides
interactive, menu-driven user input in the terminal.

Depending on the local Python version, terminal emulator, or environment setup (e.g. Anaconda on Windows),
the interactive rendering of the CLI may behave differently.
This does *not* affect the underlying application logic, data handling, analytics, or test execution.

All core functionality (habit creation, completion logging, analytics, fixtures, and tests)
can be executed and verified independently of the interactive CLI rendering.

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt

