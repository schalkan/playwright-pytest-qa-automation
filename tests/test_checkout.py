"""End-to-end UI test covering the full purchase journey:
login -> add to cart -> checkout -> order confirmation.
"""
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_checkout_flow(page: Page):
    # Arrange + Act, step by step through the real user journey
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.expect_item_count(1)
    cart_page.start_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("Devansh", "Singh", "110001")
    checkout_page.finish_order()

    # Assert: order confirmation is shown
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
