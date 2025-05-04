Feature: Task Creation
  As a user,
  I want to create new tasks
  So that I can track my work. efficiently.

  Scenario: Task Creation Redirection
    Given I am in "Home" page
    When I click on "Add New Task"
    Then I should see "Create Task" listed on the dashboard
  
  Scenario: Create New Task
    Given I am in "Create Task" page
    When I fill in "Title" with "BDD Test"
    And I fill in "Description" with "Testing Django Application"
    And I fill in "Due date" with "15-05-2025"
    And I click on "Save"
    Then I should be redirected to "Home" page
    And I should see "BDD Test" in the Home page
  
  Scenario: Create New Task
    Given I am in "Create Task" page
    When I fill in "Title" with "BDD Test 2"
    And I fill in "Description" with "2 Testing Django Application"
    And I fill in "Due date" with "15-05-2025"
    And I click on "Save"
    Then I should be redirected to "Home" page
    And I should see "BDD Test" in the Home page
  
  Scenario: Create New Task
    Given I am in "Create Task" page
    When I fill in "Title" with "BDD Test 3"
    And I fill in "Description" with "3 Testing Django Application"
    And I fill in "Due date" with "15-05-2025"
    And I click on "Save"
    Then I should be redirected to "Home" page
    And I should see "BDD Test" in the Home page