Feature: Load testing for client_register and client_login endpoints
    @regression
    Scenario: Register and login users
        Given I have endpoints for registration and login
        When I register users with random data
        When I login with random user credentials
        Then the login should succeed