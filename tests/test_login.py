"""UI tests for the SauceDemo login flow."""
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.goto()
    return lp


def test_successful_login(login_page: LoginPage, page: Page):
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_with_invalid_credentials_shows_error(login_page: LoginPage):
    login_page.login("wrong_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()


def test_login_with_locked_out_user_shows_error(login_page: LoginPage):
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_contain_text("locked out")


def test_login_with_empty_credentials_shows_error(login_page: LoginPage):
    login_page.login("", "")
    expect(login_page.error_message).to_be_visible()
