Feature: sign in to e-mail account
As a user
I want to log in
and check my e-mails

#  Scenario Outline: Log in with valid data
#Given user is on Poczta Onet website
#When user fills in the Sign In form and submits it
#Then User can see email list

  Scenario Outline: Log in with valid data

    Given user is on Poczta Onet website
    When user fills valid username <username> and valid password <password> and submits it
    Then user can see email list

    Examples:
    | username | password |
    | autografy_autografy@op.pl | ******** |
    | janek123@op.pl | haslo2 |

  Scenario Outline: Log in with invalid data
    Given user is on Poczta Onet website
    When user fills invalid username <username> and invalid password <password> and submits it
    Then user can see alert about invalid date

    Examples:
    | username | password |
    | autografy_autografy@op.pl | ******* |
    | janek123@op.pl | haslo2 |
