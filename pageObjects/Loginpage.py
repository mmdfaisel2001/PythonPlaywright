from pageObjects.Dashboard import Dashboard 


class LoginPage:
    
    def __init__(self,page):
        self.page = page
   
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
        
    def login(self, UserName, Password):
        self.page.get_by_placeholder("Username").fill(UserName)
        self.page.get_by_placeholder("Password").fill(Password)
        self.page.get_by_role("button", name = "Login").click()
        dashboard = Dashboard(self.page)
        return dashboard