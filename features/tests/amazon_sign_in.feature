Feature: Amazon Sign in tests

 Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens


 Scenario: Sign in popup is visible for a few seconds
    Given Open Amazon page
    Then Verify signin popup appears
    When wait for 8 seconds
    Then verify signin popup disappears
