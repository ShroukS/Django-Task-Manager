Feature: Bulk Tasks Actions
  As a user
  I want to select multiple tasks to complete or delete
  So that I can manage my tasks more quickly and easily

  Scenario: Mark Multiple Tasks as Completed
    Given I am in "Home" page
    When I select the tasks "BDD Test" and "BDD Test 3"
    And I click on "Mark as Complete"
    Then I should "✔ Completed" statuses for tasks "BDD Test and "BDD Test 3"

  Scenario: Delete Multiple Tasks
    Given I am in "Home" page
    When I select the tasks "BDD Test" and "BDD Test 3"
    And I click on "Delete Selected"
    Then I should not see "BDD Test" and "BDD Test 3" in "Home" page