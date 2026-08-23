Feature: Order Items
    Test related to ordering items in SauceDemo website

 Scenario Outline: Verify the items are ordered
    Given Login with <username> and <password>
    When the user selects the Products
    And click on the cart to navigate to Your Cart page
    And click checkout and user will be navigated to Checkout page
    And the user reached checkout page and Enters <FirstName>, <LastName> and <PostalCode>
    
    And the user click continue Order is succesfully placed
     
    And verify message will be displayed

    Examples:
        | username               | password     |      FirstName      | LastName|PostalCode|
        | standard_user          | secret_sauce | Mohamed Faisel Bari |  M      |603103    |  
        |performance_glitch_user | secret_sauce | Mohamed Faisel Bari |  M      |603103    |
        |  visual_user           | secret_sauce | Mohamed Faisel Bari |  M      |603103    |