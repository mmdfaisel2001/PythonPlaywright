import json
import time

from playwright.sync_api import Page, expect
import pytest



from pageObjects.Loginpage import LoginPage 
from pageObjects.Dashboard import Dashboard
from pageObjects.OrderValidation import ValidateOrder
from pageObjects.YourInformation import PersonalInformation
from pageObjects.OrdersView import OverviewPage
from pageObjects.OrderComplete import OrderComplete
from conftest import browserInstance




with open("data/credentials.json") as f:
        test_data = json.load(f)
        userCredential_list = test_data['UserCredentials']

@pytest.mark.parametrize('UserCredentials',userCredential_list)
def test_validation(page: Page, UserCredentials):
    UserName = UserCredentials["UserName"]
    Password = UserCredentials["UserPassword"]
    FirstName = UserCredentials["FirstName"]
    LastName = UserCredentials["LastName"]
    PostalCode = UserCredentials["PostalCode"]
    
    
    #Login Page
    Loginpage = LoginPage(page)
    Loginpage.navigate()
    dashboard = Loginpage.login(UserName,Password)
    
    #Products
    dashboard.create_order() 
    dashboard.click_cart()
    
    #Your Cart
    Order_Validation = ValidateOrder(page)
    Order_Validation.checkout()
    
    #Checkout: Your Information
    
    AddressDetails = PersonalInformation(page)

    AddressDetails.enter_details(
    FirstName,
    LastName,
    PostalCode
)
   
    #Checkout: Overview
    OrderDetails = OverviewPage(page)
    OrderDetails.OrdersOverview()
        
    #Checkout: Complete!
    OrderSuccessful = OrderComplete(page)
    OrderSuccessful.verify_order_complete()

    
    
    