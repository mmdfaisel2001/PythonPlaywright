class PersonalInformation():
    
    def __init__(self, page):
        self.page =page
        
       
        
    def enter_details(self, first_name, last_name, postal_code):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.get_by_placeholder("Zip/Postal Code").fill(postal_code)
        self.page.get_by_role("button",name ='Continue').click()