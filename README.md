# PyTest Learning

A hands-on learning repository for **PyTest** — covering basic assertions, fixtures (scopes, hooks), parameterization, and Playwright integration.

## Prerequisites

- Python 3.8+
- `pytest` — run `pip install pytest`
- For Playwright tests: `pip install playwright` then `playwright install`

## Project Structure

```
PyTestLearning/
├── getting_started/          # Basic pytest concepts
│   ├── test_first.py         # Assertions, string & float comparisons
│   ├── test_second.py        # Simple assertions and prints
│   └── test_third.py         # Class-based tests
├── fixtures/                 # Pytest fixture patterns
│   ├── conftest.py           # Session-scoped db_connection fixture
│   ├── test_fixture_usage.py       # Parameter fixtures (user, page_detail)
│   ├── test_fixture_webpage.py     # Multiple fixtures per test
│   ├── test_fixture_hooks.py       # Fixture setup/teardown with yield
│   └── test_fixture_hooks_for_shared_fixture.py  # Shared fixture across modules
├── parameterize/             # @pytest.mark.parametrize patterns
│   ├── calc.py               # Simple math helper functions (add, subtract, multiply)
│   ├── test_calc.py          # Parametrized tests with ids and pytest.param()
│   └── test_playwright.py    # Nested parametrize (browser × viewport) with skip marks
└── fixtures_playwright/      # Playwright + PyTest integration
    ├── conftest.py           # Session-scoped browser & module-scoped page fixtures
    ├── test_login.py         # Login flow (stub)
    └── test_employeeCreation.py  # Employee creation flow (stub)
```

## Getting Started

### Run all tests

```bash
pytest
```

### Run a specific folder

```bash
# Getting started basics
pytest getting_started/ -v

# Fixtures
pytest fixtures/ -v

# Parameterization (new!)
pytest parameterize/ -v

# Playwright integration
pytest fixtures_playwright/ -v
```

### Run with verbose output and prints

```bash
pytest -v -s
```

## What You'll Learn

### 1. Getting Started (`getting_started/`)

| Concept | File |
|---|---|
| Basic `assert` statements | `test_first.py`, `test_second.py` |
| String assertions (`in`, `startswith`, `endswith`) | `test_first.py` |
| Floating-point comparison with `pytest.approx()` | `test_first.py` |
| Class-based test organization (`class TestXxx`) | `test_third.py` |

### 2. Fixtures (`fixtures/`)

| Concept | File |
|---|---|
| Module-scoped fixtures (`@pytest.fixture`) | `test_fixture_usage.py` |
| Multiple fixtures per test | `test_fixture_webpage.py` |
| Session-scoped fixture with setup/teardown (`yield`) | `conftest.py` + `test_fixture_hooks.py` |
| Sharing fixtures across modules via `conftest.py` | `test_fixture_hooks_for_shared_fixture.py` |

**Fixture scopes covered:**
- **Function** (default) — one instance per test function
- **Module** — one instance per module file
- **Session** — one instance across the entire test run

### 3. Parameterization (`parameterize/`) — *new!*

| Concept | File |
|---|---|
| Basic `@pytest.mark.parametrize` with tuple lists | `test_calc.py` (`test_add`) |
| Custom test names via `ids=` parameter | `test_calc.py` (`test_add_id`) |
| Explicit `pytest.param()` with labeled IDs | `test_calc.py` (`test_add_param`) |
| Nested parametrize (cross-product of parameters) | `test_playwright.py` (`test_login_page`) |
| Conditional skipping with `pytest.mark.skip` via `pytest.param()` | `test_playwright.py` (`test_login_page_param`) |

**Key patterns:**
- **Basic parametrize**: `@pytest.mark.parametrize("a,b,expected", [...])` — passes each tuple as arguments
- **Custom IDs**: `ids=["positive numbers", ...]` — makes test output readable
- **pytest.param()**: `pytest.param(value, id="label", marks=...)` — adds labels and conditional marks (e.g., skip)
- **Nested parametrize**: stacking two decorators creates a cross-product of all parameter combinations

### 4. Playwright Integration (`fixtures_playwright/`)

Demonstrates chaining fixtures with different scopes:
- `browser` — session-scoped, sets up once per test run
- `page` — module-scoped, depends on `browser`, sets up once per module

| Test | Description |
|---|---|
| `test_login.py` | Login with valid credentials (stub) |
| `test_employeeCreation.py` | Employee creation flow (stub) |

## Key Takeaways

1. **Fixtures** are the backbone of reusable test setup — define them in `conftest.py` for automatic discovery.
2. **Scope matters** — choose the narrowest scope that works to keep tests fast and isolated.
3. **`yield` in fixtures** enables both setup and teardown logic (useful for DB connections, browser sessions).
4. **`pytest.approx()`** handles floating-point comparisons reliably instead of `==`.
5. **Class-based tests** let you group related test methods under a single fixture instance (class scope).
6. **`@pytest.mark.parametrize`** runs the same test logic with multiple inputs — reduces duplication dramatically.
7. **Nested parametrize** creates a cross-product of all parameter combinations (e.g., 3 browsers × 3 viewports = 9 test cases).
8. **`pytest.param()` with `marks=`** lets you conditionally skip or mark individual parameter combinations.
