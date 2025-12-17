## DAY 2

Initial planning notes during wireframe and user journey process

## To test MVP (thurs)

- `can an artist sign up?`
- `can an artist input name, genre?`
- Q: what fields are required v optional?
- Q: can create profile with minimal info?
- Q: can edit profile after creation?

- `can an artist add a tour date?`
- Q: required fields: date, venue, city? Anything else?
- Q: can add multiple dates?
- Q: can edit/delete tour dates?
- Q: how do dates display? Chronological? Upcoming only?

- `does the message/update field display/update as expected?`
- `can an artist post a message?`
- Q: text only or can add images?
- Q: character limit?
- Q: can edit/delete posts?
- Q: how do posts display? most recent first?
- Q: what if artist has no posts yet? (empty state)

- `is artist page publically visible?`
- `does artist page show profile info + tour dates + feed?`
- Q: clear and accesible layout/organisation?
- Q: what if sections are empty?

- `can a user navigate to other artist pages?`

- `is MVP accessible?`
- Q: keyboard navigable?
- Q: clear labels?
- Q: error messages helpful?
- Q: can tab through tour date/message creation?
- Q: basic design implementation clear contrast/readable?
- `are alt text descriptions present and clear?`


## To Test V2 (can create fan account and follow + Spotify API)

- `can a fan sign up?`
- Q: What's required? Email, username, password? Anything else?
- Q: Username validation - length, special characters, uniqueness?
- Q: Password requirements - minimum length, complexity?
- Q: What if email already exists? Clear error message?
- Q: what other information can a fan display on their profile? Bio? Pic?
- `can a fan link their Spotify account?`
- `is a fan's top 5 artists displayed on their profile?`
- Q: can a fan edit their profile after creation?
- Q: is a fan's profile publicly viewable or private?
- Q: Can fans see other fans' profiles?
- Q: Empty states: what if fan has no bio, no profile pic?

- `can a fan follow an artist from artist page?`
- Q: Is there a "Follow" button clearly visible on artist page?
- Q: Does button change state after following? (Follow to Following / Unfollow)
- `can a fan unfollow an artist from artist page?`
- `can a fan follow multiple artists?`
- Q: How do fans find an artist? Search? By name/genre?
- Q: Is there a limit to how many artists you can follow?
- Q: What if fan tries to follow an artist twice? (Should be prevented)
- Q: What if fan follows zero artists? (Empty state)
- Q: are the fan's followed artists displayed on their profile? Where do fans see their list of followed artists?
- Q: Can fans unfollow from this list or only from artist page?
- Q: Can fans search/filter their followed artists?
- Q: Can fans see who else follows an artist from artist page?

- `can an artist link their Spotify account?`
- Q: what information is displayed from Spotify on artist and fan pages?

- Q: Can artists see their follower count? Is it displayed on their artist profile?
- Q: Can artists see WHO their followers are?



FAN FEED
- `Does fan feed show only artists they follow?`
- Q: What appears in feed? Tour dates? Messages? Both?
- Q: Chronological order (most recent first)?
- Q: Mixed feed (all followed artists combined) or separated by artist?
- Q: Does feed auto-refresh or manual refresh?
- Q: If fan follows 10 artists and one posts 50 times, does that dominate the feed?
- `Is is clear which artist posted what?`
- Q: Can fan click through to artist page from feed?
- Q: Can fan click on tour date in feed to see gig details?
- Q: Can fan interact with posts from feed?
- Q: Is long text truncated or full display?
- `Do images display correctly in feed?`
- Q: What if fan follows zero artists? (Empty state: "Follow artists to see updates")
- Q: What if followed artists have posted nothing? (Empty state: "No updates yet")
- Q: What if fan unfollows an artist... does their content immediately disappear from feed?
- Q: Load more / pagination - how many posts load at once?



CONCERT PAGE
- Q: Details displayed? Date, venue, city, ticket link, artist's description?
- Q: only single concert pages or a searchable list of all concerts?
- `Can fan navigate to gig detail page from artist page or feed?`
- Q: Is there a section to display fan-uploaded content?
- Can anyone add photos/memories or only fans who follow that artist?
- Can fans add content before gig happens or only after?

- `Can fan upload photo to gig page?`
- Q: Required fields? Just photo, or photo + caption? (Alt text automatic field by user?)
- Q: File size/format limits?
- Q: Can upload multiple photos at once or one at a time?
- Q: Can fan edit/delete their own uploads?
- Q: Can fan see WHO uploaded each photo? (Username displayed?)
- Q: What if inappropriate content uploaded? Moderation/reporting system?
- Q: Text-only memories allowed, or must include photo?
- Q: Character limit on captions/memories?
- Q: Can include links, hashtags, mentions?
- Q: How do memories display? Grid, list, timeline?
- Q: Chronological or curated order?

- `Is there clear distinction between artist's gig info and fan content?`
- Q: How many fan photos show before "see more"?
- Q: Can fans like/react to other fans' photos?
- Q: Can fans comment on other fans' photos?
- Q: Empty state if no fan content yet? ("Be the first to share memories!")
- Q: Can artist delete fan-uploaded content from their gig page?
- Q: Can artist feature/pin certain fan photos? 
- Q: Can an arist pin fan content to their artist page?


SIGN IN PAGE

- `Can fan log in after creating account?`
- `Can fan log out?`
- Q: What if fan forgets username/email?
- Q: auto-logout?

PERMISSIONS:

- Q: What can logged-OUT users see? (Artist pages public? Feed requires login?)
- Q: If user has both artist + fan account, how do they switch?

NAVIGATION/UX

- Q: Can fan easily navigate between: feed, followed artists, profile?
- Q: Is there a "Discover" or "Browse artists" section?
- Q: Search functionality - can fans search for artists by name? How do fans FIND artists to follow initially?
- `Are menu/header and back buttons all clear?`