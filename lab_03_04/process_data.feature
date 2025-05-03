Feature: Process Data
  As a user
  I want to process data
  So that I can get the desired output

  Scenario: Use function f1
    Given I have a list of dictionaries with resume
    When I call function f1 with this list
    Then I should get a sorted list of job names

  Scenario: Use function f2
    Given I have a list of job names
    When I call function f2 with this list
    Then I should get a list of job names starting with "программист"

  Scenario: Use function f3
    Given I have a list of job names
    When I call function f3 with this list
    Then I should get a list of job names with " с опытом Python" appended