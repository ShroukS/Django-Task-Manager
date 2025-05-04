Feature: Single Tasks Edit And Delete
  As a user
  I want to edit or delete a specific task
  So that I can keep my task list accurate and up to date
  
  Scenario: Edit Single Task
    Given I am in "Home" page
    When I click on "Edit" for "BDD Test"
    Then I should be redirected to "Edit Task" page
    When I fill in "Description" with "Updated Testing Django Application Description"
    And I click on "Save"
    Then I should be redirected to "Home" page
    And I should see "Updated Testing Django Application Description" in the Home page
    
  Scenario: Delete Single Task
    Given I am in "Home" page
    When I click on "Delete" for "BDD Test 2"
    Then I should be redirected to "Delete Task" page
    When I click on "Yes, Delete"
    Then I should be redirected to "Home" page
