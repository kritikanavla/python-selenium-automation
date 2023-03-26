Feature: Amazon cart tests

    Scenario: Verify that item page opens
        Given Open Amazon HomePage
        When input kitchy pizza cutter wheel into search
        And click on item search button
        And click on the item link
        And click on Add to Cart
        And click on cart button
        Then verify that cart has 1 item