

from pytest_bdd import given, scenarios, when, parsers
from playwright.sync_api import Page

from pageObjects.OrderComplete import OrderComplete
from pageObjects.Loginpage import LoginPage
from pageObjects.Dashboard import Dashboard
# import pageObjects.OrderComplete
from pageObjects.OrderValidation import ValidateOrder
from pageObjects.OrdersView import OverviewPage
from pageObjects.YourInformation import PersonalInformation

scenarios('features/Orders.feature')


@given(parsers.parse('Login with {username} and {password}'))
def login_step(page: Page, username,password):
   

    loginpage = LoginPage(page)

    loginpage.navigate()
    dashboard = loginpage.login(username, password)
    return dashboard
@when('the user selects the Products')
def creating_order(page: Page):
    dashboard = Dashboard(page)
    dashboard.create_order()
    
@when('click on the cart to navigate to Your Cart page')
def user_selects_product(page: Page):
    dashboard = Dashboard(page)
    dashboard.click_cart()
    

    
@when('click checkout and user will be navigated to Checkout page')
def user_is_on_checkoutpage(page: Page):
    Order_Validation = ValidateOrder(page)
    Order_Validation.checkout()
    
@when(parsers.parse('the user reached checkout page and Enters {FirstName}, {LastName} and {PostalCode}'))
def  user_enters_imformation(page: Page, FirstName, LastName, PostalCode):
    
    AddressDetails = PersonalInformation(page)
    
    AddressDetails.enter_details(
    FirstName,
    LastName,
    PostalCode
    )
    
@when('the user click continue Order is succesfully placed')
def user_placed_order(page:Page):
    OrderDetails = OverviewPage(page)
    OrderDetails.OrdersOverview()
    
@when('verify message will be displayed')
def verify_order(page:Page):
    OrderSuccessful = OrderComplete(page)
    OrderSuccessful.verify_order_complete()  