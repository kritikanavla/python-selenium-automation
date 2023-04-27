Feature: Amazon cart tests

    Scenario: Verify that item page opens
        Given Open Amazon page.
        #When input kitchy pizza cutter wheel into search
        When Input text kitchy pizza cutter wheel
        And Click on search button
        And click on the item link
        And click on Add to Cart
        And click on cart button
        Then verify that cart has 1 item