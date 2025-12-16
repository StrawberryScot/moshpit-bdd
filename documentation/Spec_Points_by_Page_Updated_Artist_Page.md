KEY: 
AA = Relating to, or representing an Artist Action 
FA = Relating to, or representing a Fan Action 
FA/AA = Relating to, or representing Action by Fan and Artist (IE 'USER')?

## SIGN IN/UP PAGE
- FA/AA - `can a user sign up?`
- FA/AA - Q: What's required? Email, username, password? Anything else?
- FA/AA - Q: Username validation - length, special characters, uniqueness?
- FA/AA - Q: Password requirements - minimum length, complexity?
- FA/AA - Q: What if email already exists? Clear error message?

- FA/AA - `Can user log in after creating account?`
- FA/AA - `Can user log out?`
- FA/AA - Q: What if user forgets username/email?
- FA/AA - Q: auto-logout?

- AA - `can an artist sign up?`
- AA - `can an artist input name, genre?`
- AA - Q: what fields are required v optional?

**Assumptions here - there's a single 'user sign up' rather than separate fan and artist...**


## Fan Home Page ? - is this FEED?
## Artist Home Page? - is this Artist Page?

## ARTIST PAGE
- AA - `can an artist add a tour date?` - Y
- AA - Q: required fields: date, venue, city? Anything else? - TBD
- AA - Q: can add multiple dates? - Y
- AA - Q: can edit/delete tour dates? - Y
- AA - Q: how do dates display? Chronological? Upcoming only? - Chronological by default. Filtering?
- AA - Q: can edit artist page after creation? - Y

- AA - `can an artist post a message?` - Y (MVP)
- AA - Q: text only or can add images? - Both (Text-Only MVP)
- AA - Q: character limit? - Y. Amount?
- AA - Q: can edit/delete posts? - Y
- AA/FA - Q: how do posts display? most recent first? - Y (MVP)
- AA/FA - Q: what if artist has no posts yet? (empty state) - Y. (For user - 'No posts yet' message included.) (For artist - 'Add post' prompt?) 
- AA/FA - `does the message/update field display/update as expected?` - Y

- AA/FA - `is artist page publically visible?` - Y (MVP)
- AA/FA - `does artist page show profile info + tour dates + feed?` - Y
- AA/FA - Q: clear and accesible layout/organisation? - Y
- AA/FA - Q: what if sections are empty? - Y (N/A for MVP)
- AA - `can an artist link their Spotify account?` - Y
- AA/FA - Q: what information is displayed from Spotify on artist and fan pages? Fan pages - Top artists, badges based off of Spotify data?
- AA/FA - Q: is there a Spotify web player embedded within the artist page for the artist's music? - Y
- AA - Q: can create profile with minimal info? - N. Artist will have to complete required fields.

- AA/FA - Q: Can artists see their follower count? Is it displayed on their artist profile? - Y
- AA - Q: Can artists see WHO their followers are? - Y
- FA - Q: Can fans see who else follows an artist from artist page? - TBD, depending on implementation of public/private pages?
- FA - Q: What if fan tries to follow an artist twice? - Should be prevented. If fan follows artist, only presented with 'Unfollow' button.

- FA - `can a fan follow an artist from artist page?` - Y
- FA - Q: Is there a "Follow" button clearly visible on artist page? - Y for fans. N for artists.
- FA - Q: Does button change state after following? (Follow to Following / Unfollow) - Y
- FA - `can a fan unfollow an artist from artist page?` - Y
- FA - `can a fan follow multiple artists?` - Y
- FA - `can a user navigate to other artist pages?` - Y.

## FAN ACCOUNT PAGE / PROFILE

- FA - Q: what other information can a fan display on their profile? Bio? Pic?
- FA - `can a fan link their Spotify account?`
- FA - `is a fan's top 5 artists displayed on their profile?`
- FA - Q: can a fan edit their profile after creation?
- FA - Q: is a fan's profile publicly viewable or private?
- FA - Q: Can fans see other fans' profiles?
- FA - Q: Empty states: what if fan has no bio, no profile pic?

- FA - Q: Can fans search/filter their followed artists?
- FA - Q: What if fan follows zero artists? (Empty state)
- FA - Q: are the fan's followed artists displayed on their profile? Where do fans see their list of followed artists?
- FA - Q: Can fans unfollow from (potential) list of follows or only from artist page?
- FA - Q: Is there a limit to how many artists you can follow?

## FAN FEED
- FA - `Does fan feed show only artists they follow?`
- FA - Q: What appears in feed? Tour dates? Messages? Both?
- FA - Q: Chronological order (most recent first)?
- FA - Q: Mixed feed (all followed artists combined) or separated by artist?
- FA - Q: Does feed auto-refresh or manual refresh?
- FA - Q: If fan follows 10 artists and one posts 50 times, does that dominate the feed?
- FA - `Is is clear which artist posted what?`
- FA - Q: Can fan click through to artist page from feed?
- FA - Q: Can fan click on tour date in feed to see gig details?
- FA - Q: Can fan interact with posts from feed?
- FA - Q: Is long text truncated or full display?
- FA - `Do images display correctly in feed?`
- FA - Q: What if fan follows zero artists? (Empty state: "Follow artists to see updates")
- FA - Q: What if followed artists have posted nothing? (Empty state: "No updates yet")
- FA - Q: What if fan unfollows an artist... does their content immediately disappear from feed?
- FA - Q: Load more / pagination - how many posts load at once?

## INDIVIDUAL GIG/CONCERT PAGE
- FA/AA - Q: Details displayed? Date, venue, city, ticket link, artist's description?
- FA/AA - Q: only single concert pages or a searchable list of all concerts?
- FA - `Can fan navigate to gig detail page from artist page or feed?`
- FA - Q: Is there a section to display fan-uploaded content?
- FA - Can anyone add photos/memories or only fans who follow that artist?
- FA - Can fans add content before gig happens or only after?
- FA - `Can fan upload photo to gig page?`
- FA - Q: Required fields? Just photo, or photo + caption? (Alt text automatic field by user?)
- FA - Q: File size/format limits?
- FA - Q: Can upload multiple photos at once or one at a time?
- FA - Q: Can fan edit/delete their own uploads?
- FA - Q: Can fan see WHO uploaded each photo? (Username displayed?)
- FA - Q: What if inappropriate content uploaded? Moderation/reporting system?
- FA - Q: Text-only memories allowed, or must include photo?
- FA - Q: Character limit on captions/memories?
- FA - Q: Can include links, hashtags, mentions?
- FA - Q: How do memories display? Grid, list, timeline?
- FA - Q: Chronological or curated order?

- FA/AA - `Is there clear distinction between artist's gig info and fan content?`
- FA - Q: How many fan photos show before "see more"?
- FA - Q: Can fans like/react to other fans' photos?
- FA - Q: Can fans comment on other fans' photos?
- FA - Q: Empty state if no fan content yet? ("Be the first to share memories!")
- AA - Q: Can artist delete fan-uploaded content from their gig page?
- AA - Q: Can artist feature/pin certain fan photos? 
- AA - Q: Can an arist pin fan content to their artist page?

## List of Gigs Page?

## List of Artists Page / Artist Search / Discover Page?


- Q: How do fans find an artist? Search? By name/genre?


GENERAL

## ACCESSIBILITY

- Q: keyboard navigable?
- Q: clear labels?
- Q: error messages helpful?
- Q: can tab through tour date/message creation?
- Q: basic design implementation clear contrast/readable?
- `are alt text descriptions present and clear?`

NAVIGATION/UX

- Q: Can fan easily navigate between: feed, followed artists, profile?
- Q: Is there a "Discover" or "Browse artists" section?
- Q: Search functionality - can fans search for artists by name? How do fans FIND artists to follow initially?
- `Are menu/header and back buttons all clear?`

PERMISSIONS:

- Q: What can logged-OUT users see? (Artist pages public? Feed requires login?)
- Q: If user has both artist + fan account, how do they switch?
