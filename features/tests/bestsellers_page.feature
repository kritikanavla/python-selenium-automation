Feature: Amazon bestseller tests

    Scenario: Best Sellers has correct amount of links
        Given Open Amazon home
        When click on Best Sellers
        Then Verify that there are 5 links
