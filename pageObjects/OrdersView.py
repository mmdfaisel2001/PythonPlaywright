class OverviewPage:
    
    def __init__(self, page):
        self.page = page
        
    def OrdersOverview(self):
        self.page.get_by_role("button",name ='Finish').click()