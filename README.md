# Playwright QA Automation Suite

![Tests](https://github.com/schalkan/playwright-pytest-qa-automation/actions/workflows/tests.yml/badge.svg)

An end-to-end UI and API test automation suite built with Playwright and Python, demonstrating the Page Object Model, pytest fixtures, API testing, and CI integration.

## What this covers

**UI tests** (against [saucedemo.com](https://www.saucedemo.com), a public QA practice site):
- Login: valid login, invalid credentials, locked-out user, empty fields
- Cart: adding single/multiple items, removing items
- Full checkout flow: login -> add to cart -> checkout -> order confirmation

**API tests** (against [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)):
- GET requests and response validation
- POST / PUT / DELETE and status code verification

## Structure

```
pages/        Page Object Model classes (one per page/flow)
tests/        Test files + shared pytest fixtures (conftest.py)
.github/      CI workflow (GitHub Actions)
```

## Why Page Object Model

Each page's locators and actions live in one class, so if the UI changes, the fix happens in one place instead of across every test that touches that page. Tests stay focused on *what* is being verified, not *how* to find each element.

## Running locally

```bash
pip install -r requirements.txt
playwright install chromium
pytest                       # run everything, headless
pytest --headed               # watch it run in a real browser
pytest tests/test_login.py -v # run one file, verbose
```

## CI

Every push runs the full suite via GitHub Actions. On failure, a Playwright trace is uploaded as an artifact for debugging.
