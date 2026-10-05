"""Page Object for the SauceDemo inventory (products) page."""


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_item_to_cart(self, item_name: str):
        # Scope to the one product card whose title matches item_name,
        # then click the "Add to cart" button inside that specific card.
        self.page.locator(".inventory_item").filter(has_text=item_name).get_by_role(
            "button", name="Add to cart"
        ).click()

    def remove_item_from_cart(self, item_name: str):
        self.page.locator(".inventory_item").filter(has_text=item_name).get_by_role(
            "button", name="Remove"
        ).click()

    def go_to_cart(self):
        self.cart_link.click()
