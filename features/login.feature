Feature: OrangeHRM Login Authentication

  @login @smoke
  Scenario: Successful login with valid credentials
    Given the user is on the OrangeHRM login page
    When the user logs in with username "Admin" and password "admin123"
    Then the user should be redirected to the dashboard
