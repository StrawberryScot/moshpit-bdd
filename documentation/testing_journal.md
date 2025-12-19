# Kathy Peacock & Benjamin Loveday Final Project TESTING JOURNAL

## WEEK 1

## DAY 1 

- full team meeting all day, contributing ideas for project and narrowing down on MVP, explaining purpose and contributions of QE team. Setting some communication and requirements/requests from our side looking forward...

- decided on standards for bug reporting and enhancement suggestions etc. To that goal made templates for GitHub issues. We also contributed documentation of standards for git branch and commit naming conventions, and shared our perspectives on the importance of accessibility considerations from start.

- We talked about the importance of effective and clear element naming - HTML id etc - both for accessibility and test automation purposes.
 

## DAY 2 

- Finalising scope of MVP. Devs had conversation about styling, wanting to do it all at the very end. We were able to confidently push back and come to a compromise that everyone agreed with, explaining accessibility and UX implications and the need for us to at least have clear expectations/plan regarding styling before the last minute to raise questions/concerns/create plans etc.

- We sent over some 'designing with accessibility in mind' resources.

- The devs were made aware that we can create csv datasets etc, if necessary.

- We strongly pushed for a feature implementation roadmap so we don't raise unnecessary issues and bugs for features/functionality that are planned for future updates.

- The devs had not come up with a Spec, informal or otherwise - so, we worked towards this by creating a document containing expected user actions, and mainly consisting of assumptions and questions regarding features, functionality, display and UX details. This was then sorted into sections by PAGE and 
annotated as to whether it refers to Artist or Fan actions, or both. This was helpful in informing decision-making around artist/fan account, action and view distinctions. We went through the ARTIST PAGE section as a team (ie the MVP) making sure there was clear understanding for all around what is expected and when (ie Yes, No, Not Yet). This means we'll be able to plan tests accordingly, and preempt a lot for the devs.

- A BDD repo was created, including basic scenarios and step definitions for the MVP. (Gherkin .feature and step defs in Java) We can now flesh out BDD tests and documentation as we get more concrete user stories for new features.

- we discussed the suitability of different test techniques looking ahead, now we have a bit of spec clarity...


## DAY 3

- nice reflection with devs at standup about the value of spec questions document to ensure all on the same page from both sides of the team. Also nice to reflect on the value QEs can bring to the planning process.

- MVP dropped and there was a disjunct with what was implemented/present to the said spec doc and wireframe etc.

- useful chat with Paul about how to navigate this relationship and early stage unsurety. We appreciated his grounding direction. Helpful advice included:
-- to interrogate concerns as to whether it directly impacts our work as testers, or if it is more personal/process frustration.
-- to trust the process as devs are also in learning boat with us!
-- to practice being ok with things feeling off piste or out of our control! Sometimes this will just be how it is and often it rights itself quickly
-- consider balance between how many questions we should ask in a manner that is product-focussed, and 
take a step back to focus on planning, generating test data etc.
-- make use of the Git Project kanban system. There may be times when it's just easier/more appropriate to search for answers re SDLC etc ourselves. 

- MVP updated dropped, now with text message post functionality (and questions answered by devs which helped us feel more in control.) We were excited to finally be able to test tangibly and enjoyed an afternoon of paired exploratory and manual testing.

- First bug reports logged, and QE Report system implemented to keep team up to date in appropriately brief fashion! 


## DAY 4

- Today while we waited for new functionality we took the time to ask a few questions and get a lot of
test data generated/random generation scripts prepared. We enjoyed exploring the Faker codebase for
possibilities for our fan name and location fields (tbd). We managed to get a good collection of different
scripts and languages with a formatted csv. We also found a fun bug within the Faker code itself:

### Test Data Generation Issue

    - **Issue Found:** Faker's lt_LT (Lithuanian) locale generates names with commas in format "Surname, Firstname" which is not a valid Lithuanian naming convention and had consequences for our generated csv!

    - **Root Cause:** Investigated Faker source code - lt_LT provider has hardcoded format `'{{last_name}}, {{first_name}}'` in formats tuple.

    - **Validation:** Research confirmed Lithuanian names follow `FirstName LastName` format with no commas. The surname-first comma format is not used in Lithuanian naming conventions.

    - **Impact:** Affects CSV parsing and data validation testing.

    - **Resolution:** Decided to remove lt_LT from locales after checking there was no unique characters we'd be missing out on (special chars mostly represented in Czech data).

    - **Learning:** Even established test data generators can have bugs. Always validate generated data against real-world conventions - and check generated data in file for hidden issues!


## DAY 5

- now we have working versions that include some field validation, and basic versions of fan feed, fan page,
search function etc.

- we checked everything to make sure basic functionality as expected was working. Due to lack of new 
features that we can perform manual or automated tests on, we focussed on really nailing down a formal
spec (draft 1) so that when we come back from the break, there are no question marks and goals are 
both clearly set, and easily ticked off from both the developers' and test team perspective.
Kathy drafted up the spec against the dynamic spec questions team document.

- Kathy adapted the Faker test data script prepared so it now reflects what we can now see as an expected location input format through current hard coding. Country data was added to the users dataset generation code, per locale and in the correct user language, and csv regenerated. This means we have more rigorous i18n testing and a full set of test data ready for Selenium automation.

- Ben focussed today on exploring the code base and full backend, uncovering some interesting observations and some concerns to keep an eye on. and did some exploratory testing of the pages, both front and back end to test functionality and earmark potential issues as further things are implemented (eg with image uploading validation). 

- Ben also streamlined the issues-raising team processes; the final week is going to get very busy as a lot more core functionality drops and is pieced together, so with clear labelling etc, efficiency is optimised.

- We explored the testing potential of the tool SonarQube, using the product in its basic current state to practice gathering intel on security, authentication, maintenance, and unit test coverage. We made note of some of the code syntax concerns etc, but will not consider it a priority for devs at this stage. One issue was raised as an enhancement concerning the length of one of the controllers.

- finally we planned all test areas we need to cover after the break, including scenarios and actions to run, tools and data, and method ideas. And a final stand up with the team before 2 weeks off!


## WEEK 2

