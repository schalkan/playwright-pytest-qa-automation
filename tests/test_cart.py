"""UI tests for the SauceDemo cart flow."""
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def inventory_page(page: Page):
    # Arrange: start every cart test already logged in on the inventory page
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


def test_add_single_item_to_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_add_multiple_items_to_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bike Light")
    expect(inventory_page.cart_badge).to_have_text("2")


def test_remove_item_from_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.remove_item_from_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_count(0)
