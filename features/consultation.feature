Feature: See all products in my store

@test
    Scenario: 
        Given I have a store
        When I get all the products
        Then I check and validate all products
