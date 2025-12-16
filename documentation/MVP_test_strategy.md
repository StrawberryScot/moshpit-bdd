# Test Strategy For MVP (Artist Page):

**In Scope:** 
- public artist page viewing
- artist details visible (name, genre)
- artist can post a message (text only)
- display of text message posts (ordering etc)
- initial accessibility assessment

**Out of Scope**
- adding and editing tour dates
- display of tour dates
- artist can edit page
- artist can post a message (image)
- artist can edit and delete posts
- 'no post yet' - empty state handling
- empty space handling eg gigs list N/a for MVP
- spotify linking and displaying
- spotify web player
- following an artist
- follower count + any display re followers

- any other pages inc. user sign up, fan profile and feed, individual gig pages, fan interaction and posting of content.


*scope questions*
- is character limit for text message posts in MVP?
- does an artist have a different view of their own artist page than the fan?
- is MVP pre-seeded artists or artist creation of artist page? (ie are we able to test inputs/fields/error-handling?)



## Test Types:

Manual exploratory testing
BDD automated tests
Accessibility spot checks


**Entry Criteria:**
Artist can sign up and create profile (check if sign up is in scope for MVP)
Test team has access to environment, seed data and any permissions.

**Exit Criteria:**
Artist page displays with expected artist details, and with more than one one message post. 

**Risks:** styling TBD, potential database issues (preseeding etc), lots of upcoming functionality not yet implemented.