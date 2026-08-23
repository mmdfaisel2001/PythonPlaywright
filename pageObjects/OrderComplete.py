from playwright.sync_api import expect

class OrderComplete:
    def __init__(self, page):
        self.page = page
        
    def verify_order_complete(self):
        expect(self.page.locator(".complete-header")).to_contain_text("Thank you for your order!") 
        
        
    def download_order_pdf(self):
        with self.page.expect_download() as download_info:
            self.page.get_by_role(
                "button",
                name="Generate PDF order"
            ).click()

        return download_info.value      