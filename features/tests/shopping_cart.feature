Feature: Amazon Shopping cart test
  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify "Your Shopping Cart is empty." text present
