Feature: Google searching
  As an user,
  I want to search "panda" in Google
  so I can see searching results

  Scenario: Search from the search bar

    Given a web browser is at the Google home page
    When the user enters "panda" into the search bar
    Then links related to "panda" are shown on the results page


  Scenario: Image search

    Given Google search results for "panda" are shown
    When the user clicks on the "Images" link at the top of the results page
    Then images related to "panda" are shown on the results page


  Scenario: Simple Google search

    Given a web browser is on the Google page
    When the search phrase "panda" is entered
    Then results for "panda" are shown
    And the following related results are shown
      | related       |
      | Panda Express |
      | giant panda   |
      | panda videos  |


  Scenario Outline: Simple Google searches
    Given a web browser is on the Google page
    When the search phrase "<phrase>" is entered
    Then results for "<phrase>" are shown
    And the related results include "<related>"

    Examples:
      | phrase   | related       |
      | panda    | Panda Express |
      | elephant | Elephant Man  |
