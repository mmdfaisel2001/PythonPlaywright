from pageObjects.OrderValidation import ValidateOrder

class Dashboard:
    
    def __init__(self,page):
        self.page = page
        
    def click_cart(self):
        self.page.locator(".shopping_cart_link").click()
        
    def add_product(self, product_name):
        product = self.page.locator(".inventory_item").filter(
        has_text=product_name
    )
        product.get_by_role("button").click()    
        
    def create_order(self):
        self.add_product("Sauce Labs Backpack")
        self.add_product("Sauce Labs Fleece Jacket")
        self.add_product("Sauce Labs Onesie")    
        OrderValidation = ValidateOrder(self.page)
        return OrderValidation