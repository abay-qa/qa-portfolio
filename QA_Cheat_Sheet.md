# QA Engineering Cheat Sheet
*Your personal reference guide — save this and use it anytime!*

---

## 1. Bug Report Template

| Field | What to write |
|-------|--------------|
| Title | Short, clear summary of the problem |
| Steps to Reproduce | Exact steps to make the bug happen again |
| Expected Result | What should have happened |
| Actual Result | What actually happened |
| Severity | Critical / High / Medium / Low |
| Environment | Browser, OS, Device |
| Attachments | Screenshots or screen recordings |

### Severity Levels
| Level | Meaning | Example |
|-------|---------|---------|
| Critical | App is unusable | App crashes on launch |
| High | Major feature broken | Can't complete a purchase |
| Medium | Feature works but poorly | Wrong error message shown |
| Low | Minor cosmetic issue | Button color is off |

---

## 2. Types of Testing

| Type | Key Question | When |
|------|-------------|------|
| Smoke | Is anything catastrophically broken? | After every new build |
| Functional | Does each feature work? | During development |
| Regression | Did we break anything existing? | After every change |
| Sanity | Does this specific fix work? | After a bug fix |
| UAT | Are real users happy? | Before release |
| Integration | Do components work together? | During/after development |

---

## 3. SDLC Phases

Plan → Requirements → Design → Develop → Test → Release → Maintain

### Waterfall vs Agile
| | Waterfall | Agile |
|--|-----------|-------|
| Style | Sequential | Short sprints (2 weeks) |
| Flexibility | Low | High |
| QA involvement | End only | Throughout |
| Used by | Legacy projects | Most modern tech companies |

### Key Agile Terms
| Term | Meaning |
|------|---------|
| Sprint | A short 2-week work cycle |
| Standup | Daily 15-min team meeting |
| Backlog | List of features/tasks to be done |
| Story | A feature from the user's perspective |
| Retrospective | Meeting to reflect on what went well/poorly |

---

## 4. API Testing

### HTTP Methods
| Method | What it does | Success Code |
|--------|-------------|-------------|
| GET | Read/retrieve data | 200 |
| POST | Create new data | 201 |
| PUT | Update existing data | 200 |
| DELETE | Remove data | 200 |

### Status Codes
| Code | Meaning |
|------|---------|
| 200 | OK — everything worked |
| 201 | Created — new data was created |
| 400 | Bad Request — wrong data sent |
| 401 | Unauthorized — not logged in |
| 403 | Forbidden — logged in but no permission |
| 404 | Not Found — resource doesn't exist |
| 500 | Server Error — something broke on the server |

### Practice API
Base URL: https://jsonplaceholder.typicode.com
GET a user:       GET /users/1
GET all users:    GET /users
Sad path (404):   GET /users/99999
Create a post:    POST /posts

---

## 5. Postman Quick Reference

1. Open Postman → Click New → Select HTTP Request
2. Choose method: GET / POST / PUT / DELETE
3. Enter the URL
4. For POST: Click Body → raw → JSON → paste your JSON
5. Click Send
6. Check the status code and response body

---

## 6. Python Basics for QA

### Variables & Data Types
name = "Abay"          # String (text)
age = 25               # Integer (number)
is_logged_in = True    # Boolean (True or False)

### Conditions
status_code = 200
if status_code == 200:
    print("Test passed!")
else:
    print("Test failed!")

### Functions
def check_status_code(actual, expected):
    if actual == expected:
        print("Test passed!")
    else:
        print("Test failed!")

---

## 7. Pytest

### Install
pip3 install pytest

### Check version
pytest --version

### Writing Tests
def test_successful_response():
    status_code = 200
    assert status_code == 200

### Running Tests
pytest qa_tests.py
pytest tests/ -v

### Pytest Output Symbols
. = Test passed
F = Test failed
E = Test had an error

---

## 8. Automated API Testing

### Install requests library
pip3 install requests

### Basic API Test
import requests

def test_get_user_success():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_get_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/99999")
    assert response.status_code == 404

---

## 9. SQL for QA

### CRUD Operations
SELECT * FROM users;                          -- Read all
SELECT * FROM users WHERE age > 30;           -- Filter
SELECT COUNT(*) FROM users;                   -- Count rows
INSERT INTO users (name, email, age) VALUES ("Abay", "email@gmail.com", 49);
UPDATE users SET age = 50 WHERE name = "Abay";
DELETE FROM users WHERE name = "John";

### LIKE and Wildcards
SELECT * FROM users WHERE email LIKE "%@gmail.com";  -- ends with
SELECT * FROM users WHERE name LIKE "A%";             -- starts with
SELECT * FROM users WHERE email LIKE "%gmail%";       -- contains

### SQLite Commands
sqlite3 qa_practice.db    -- open/create database
.tables                   -- show all tables
.exit                     -- exit SQLite

---

## 10. Terminal Commands (Mac)

| Command | What it does |
|---------|-------------|
| python3 --version | Check Python is installed |
| python3 | Open Python interactive mode |
| exit() | Exit Python interactive mode |
| touch qa_tests.py | Create a new file |
| open -e qa_tests.py | Open file in TextEdit |
| python3 qa_tests.py | Run a Python file |
| pytest qa_tests.py | Run tests with Pytest |
| pip3 install requests | Install requests library |
| pip3 install pytest | Install Pytest |
| sqlite3 db.db | Open SQLite database |

## 11. Git Commands

| Command | What it does |
|---------|-------------|
| git clone URL | Download repo from GitHub |
| git add . | Stage all changes |
| git commit -m "message" | Save a checkpoint |
| git push | Upload to GitHub |
| git pull | Download latest changes |
| git status | See what changed |
| git remote -v | Check remote URL |