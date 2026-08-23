class ValidateOrder:
    
    def __init__(self, page):
        self.page = page
        
    def checkout(self):
        self.page.get_by_role("button", name ='Checkout').click()
            