"""Page Object for the SauceDemo cart page."""
from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.cart_items = page.locator(".cart_item")

    def item_count(self) -> int:
        return self.cart_items.count()

    def expect_item_count(self, expected: int):
        expect(self.cart_items).to_have_count(expected)

    def start_checkout(self):
        self.checkout_button.click()
