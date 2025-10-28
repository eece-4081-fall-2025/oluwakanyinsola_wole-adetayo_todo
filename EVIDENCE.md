# Evidence of Development Environment

**Project:** Django Todo App

- **OS:** macOS 13.6 (example: replace with your exact version)
- **Python version:** 3.11.7
- **Virtual environment:** .venv (created with `python -m venv .venv`)
- **Django version:** 5.2.6
- **Commands run:**
  - `pip install -r requirements.txt`
  - `python manage.py makemigrations five`
  - `python manage.py migrate`
  - `python manage.py runserver`
- **Files of interest:**
  - five/models.py  (Todo model)
  - five/migrations/0001_initial.py
  - README.md
  - EVIDENCE.md



Evidence of TDD Cycles
Cycle 1 – Create and List Tasks

Goal: Implement task creation and listing.

RED: Wrote a failing test for task creation (test_create_task_minimal).

GREEN: Added task_create view and route, created the model, and confirmed tests passed.

Commit:
TDD Cycle 1 (RED→GREEN): create & list tasks for MVP

Test Evidence:
Output showed 2 passing tests (after cycle 1).

Cycle 2 – Edit, Delete, Toggle, and Move

Goal: Extend CRUD operations and test task manipulation routes.

RED: Added failing tests for edit, delete, toggle, and move routes.

GREEN: Implemented corresponding views and updated URLs.

Commit:
Cycle 2 progress: add edit/delete/toggle + move routes and minimal views (GREEN)

Test Evidence:
Output showed all 6 tests passing.

MVP Delivery

Implemented Epic 1: Task Flow with working UI (five/index.html).

All tests pass:

Ran 6 tests in 0.016s
OK


Final commit:
MVP: deliver Epic 1 (create/edit/delete/toggle with minimal UI)