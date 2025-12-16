package moshpit;

import io.cucumber.java.PendingException;
import io.cucumber.java.en.*;
import com.microsoft.playwright.*;

import static org.assertj.core.api.Assertions.assertThat;

public class StepDefinitions {

    private String artistName = "";

    @Given("an artist named {string}")
    public void anArtistNamed(String givenArtistName) {
        artistName = givenArtistName;
    }

    @Given("I am on the artist page")
    public void iAmOnTheArtistPage() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @When("I scroll to the top of the page")
    public void iScrollToTheTopOfThePage() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @Then("the artist name, bio and genre is visible")
    public void theArtistNameBioAndGenreIsVisible() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @When("I submit a post with the text {string}")
    public void iSubmitAPostWithTheText(String arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @Then("a new post with the text {string} should appear at the top of the feed")
    public void aNewPostWithTheTextShouldAppearAtTheTopOfTheFeed(String arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @When("I submit a post with the {int} characters")
    public void iSubmitAPostWithTheCharacters(int arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @Then("a new post with {int} characters should appear at the top of the feed")
    public void aNewPostWithCharactersShouldAppearAtTheTopOfTheFeed(int arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @And("there are {int} posts on the page")
    public void thereArePostsOnThePage(int arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @When("I submit a post with empty input field")
    public void iSubmitAPostWithEmptyInputField() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @Then("no new post should appear")
    public void noNewPostShouldAppear() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @And("an warning message should appear with text {string}")
    public void anWarningMessageShouldAppearWithText(String arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @When("I submit a post with {int} characters")
    public void iSubmitAPostWithCharacters(int arg0) {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }

    @And("the character count should be displayed")
    public void theCharacterCountShouldBeDisplayed() {
        // Write code here that turns the phrase above into concrete actions
        throw new PendingException();
    }
}
