"""Shared pytest fixtures for the suite."""
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    """A standalone API request context -- no browser involved.
    Used by the API test suite (test_api.py).
    """
    context = playwright.request.new_context()
    yield context
    context.dispose()
