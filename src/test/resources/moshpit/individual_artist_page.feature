Feature: Individual artist page

  Background:
    Given an artist named "HayleyWilliams"

  Scenario: Looking at the top of the page
    Given I am on the artist page
    When I scroll to the top of the page
    Then the artist name, bio and genre is visible
    And the artist name is in the page title

  Scenario: Creating a new post on an empty feed
    Given I am on the artist page
    When I submit a post with the text "hello"
    Then a new post with the text "hello" should appear at the top of the feed

  Scenario: Creating a new post exactly on the character limit on an empty feed
    Given I am on the artist page
    When I submit a post with the 200 characters
    Then a new post with 200 characters should appear at the top of the feed

  Scenario Outline: Creating a new post on a feed with preexisting posts
    Given I am on the artist page
    And there are 5 posts on the page
    When I submit a post with the text "<post_content>"
    Then a new post with the text "<post_content>" should appear at the top of the feed
    Examples:
      | post_content |
      | oneword |
      | UpperAndLower |
      | 123 |
      | alphanumeric123 |
      | two words |
      | !@£$%^&*()-_:;"'{}[]<>/ |


  Scenario: Attempting to create an new post on the feed with empty input field
    Given I am on the artist page
    When I submit a post with empty input field
    Then no new post should appear
    And an warning message should appear with text "Post is empty. Please write something before submitting it!"

  Scenario: Attempting to create an new post on the feed exceeding the character limit
    Given I am on the artist page
    When I submit a post with 201 characters
    Then no new post should appear
    And the character count should be displayed
    And an warning message should appear with text "Post is over the character limit. Please shorten the post before submitting it!"