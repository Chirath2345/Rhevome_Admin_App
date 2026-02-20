# Worklenz React — Test Automation 🧪

## Project overview 🔍
This repository contains automated UI tests that cover core Worklenz flows such as signup (including Google), login, project and task creation, task-drawer features, Kanban interactions, and responsiveness checks. Coverage focuses on UI features; integrations, billing, and complex multi-user scenarios are not fully covered.

## Tech stack ⚙️
- Python 3.11+
- Playwright (Python) — browser automation
- pytest — test runner
- pytest-playwright — Playwright fixtures for pytest
- pytest-html — HTML test reports
- Faker — test data generation
- Optional: Playwright Test config (TypeScript) present for reference

## Folder structure 📁
- `config/` — configuration files and credentials
- `pages/` — page objects (BasePage + per-page modules)
- `tests/` — pytest test suites organized by feature
- `utilities/` — helpers and utility functions (config reader, mail reader, responsive utils)
- `test_data/` — reusable test data
- `reports/` — generated test reports (`report.html`)
- `playwright-report/` — Playwright report artifacts (if generated)

Example:
```
config/
pages/
tests/
utilities/
reports/
playwright-report/
```

## Setup steps (step-by-step) 🛠️
1. Install Python 3.11+ and ensure `python` is in your PATH.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows CMD
.\.venv\Scripts\activate.bat
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
python -m playwright install
```

5. (Optional) Update config values in `config/config.ini` (e.g., `baseURL`, test `email` and `password`) if you need to point to a different environment or use other credentials.

6. Ensure any external dependencies (e.g., Mailinator credentials or other test accounts) are accessible from your network.

## How to run tests ▶️
- Run the full test suite:

```bash
pytest
```

- Run a single test file:

```bash
pytest tests/home/test_home_create_project_drawer.py -q
```

- Run tests in a folder (e.g., login tests):

```bash
pytest tests/login -q
```

- Run tests and generate HTML report:

```bash
pytest --html=reports/report.html
```

- Run a single test by keyword:

```bash
pytest -k "create_project" -q
```

- Run tests in headed mode or debug locally (set environment variables or modify fixtures to disable headless mode). Example (if fixtures support it):

```bash
HEADLESS=false pytest -s tests/...
```

(Adapt to your environment or custom fixtures as needed.)

## Known limitations / flaky areas ⚠️
- Third-party integrations (e.g., Google sign-in) can be flaky and are sensitive to external changes and rate limits.
- Email-based tests (Mailinator) may be intermittent due to mail delivery delays.
- Timing issues and network instability can cause occasional timeouts. Increase waits/timeouts in flaky areas if needed.
- Tests that depend on shared state can fail when run in parallel or without proper cleanup — prefer isolated test data and cleanup.
- Selector sensitivity: UI changes can break selectors; prefer resilient selectors and update page objects when UI changes.