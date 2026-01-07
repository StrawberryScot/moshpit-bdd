# Accessibility Assessment - Screenreader/Keyboard Navigation
*Prototype, pre-CSS styling (6.1.26)*


At a suitable mid-point in development we have run some exploratory accessibility tests on the app as it stands (pre proper CSS styling, but with core functionality). A focus on screenreader and keyboard navigation is appropriate at this stage, as we do not expect styling to impact greatly on overall element structure. 

It's been valuable to be able to demonstrate to the team of developers how some of the basic principles of accessibility design work in practice, on their own build. The screenshots show exactly what information a user who relies on a screenreader would receive when navigating through page elements - some examples of good practice seen clearly in action, and some areas we will be flagging as issues on Github to be adapted as a priority.


## VOICEOVER Exploratory Test (In-built Mac Screenreader) 


### **Navigation Bar `link list`**

The 2nd and 3rd navbar links are flagged as part of a list, which does not include the 1st link (should be streamlined).

![navigation bar links screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_14.png)



### **Navigation Bar `Profile Picture Dropdown Menu` inaccessible**

When navigating using Voiceover, there is no indication that the profile image in the top right corner holds a dropdown menu. This renders it inaccessible, and a priority critical issue to be fixed. 

![profile picture dropdown screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_9.png)


### **Navigation Bar `Search` results misleading headings**

Confusing location of the message `Found 1 result(s)` and search results filter headings.
This ties in to a wider UX issue of lack of consistency in the search results content. Most effective across the filtered responses would be separate headings for artist, user, etc. With a message for each, especially when one or both filter categories is in empty state.
When accessibility is considered here, it becomes even more pressing to have clear and consistent categorisation of search and filtering results as the impact is on both visual clarity and hidden naming descriptors and navigation.
The screenshot below shows how the message `Found 1 result(s)` appears under *Users* but is actually referring to the 1 *Artists* result displayed.

![search results screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_8.png)


### **Navigation Bar `Search` results unnecessary descriptor**

Secondary, lower priority issue: `moshpit, web content` is unnecessary text for screenreader.

![search results screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_10.png)



### **Concert Page section element naming: `Complementary`**

The right hand column/container section is labelled as a `Complementary`. (Under the interactive element heading of `Landmarks` when hovering over `Crowd` also - see screenshot below.)

Please look into more comprehensible descriptive labelling here with screenreader navigation in mind. See screenshot below.

![complementary screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_1.png)

![landmarks complementary screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_4.png)


### **Concert Page element naming: `Concert Window` and `Concert Groups`**

See screenshot below. This can be looked into further in future tests.

![window groups screenshot](/issues%20logs%20and%20resources//screenshots_accessibility_intro/screenreader_5.png)


### **Concert Page `RSVP Toggle Button`**

When using screenreader, user has no indication of whether button is toggled or not.

General UX request to add a clear user message above this button, eg. `Click here to confirm you're going, and to be added to the Crowd!`

See screenshot: 

![toggle screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_7.png)

NB screenshot of our Dev Inspect investigation of this toggle button below:

![inspect elements toggle screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/inspect_1.png)



### **Concert Page `Concert Image` and `User Profile Avatar Images`**

Concert image needs proper alt text handling for both uploaded and empty state (this also goes for *user profile picture*). 

In the `Crowd` tab for example, there's a gallery of user profile avatars which the screenreader will tab through. 

It would be best practice to have 'empty' alt text for each tile :  `alt=""`

This tells the screenreader to skip alt text reading, and just read out that it's a **picture** and a **link** with a username associated. In this example, the reader tells us we have arrived on a `list`, and for each avatar it currently reads out the class and alt. In this case it results in the username being read out twice - see screenshot below.

![avatar screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_6.png)


NB This also highlights importance of empty state text in main body. An example of this working well is in Gallery Tab with the clear brief message 'No media yet'. This means a user with a screenreader is clear there's no 'gallery' content they're just not finding etc. (As well as being generally useful and clear for all users.)


### **Artist Page `upcoming dates` items**

Concert links are each in their own individual list - to be looked into!

![concert links screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_11.png)


### **Artist Page `header`**

`heading level 1` should read `artist name` for clarity.

![artist name screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_13.png)


### **User Profile Page `page name`**

In the case of our example user 'bob', the screenreader describes the overall page as `bob`, rather than the more accurate/helpful `bob user page`.

![user page screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_12.png)


### **User Profile Page `element interaction dropdown`**

Either `banner` or `navigation` is redundant; only one of the two needs to be selectable. Please see screenshot below:

![profile page dropdown screenshot](/issues%20logs%20and%20resources/screenshots_accessibility_intro/screenreader_15.png)


## WAVE - accessibility evaluation tool - Chrome extension


Wave analysis of Individual Concert Page pointed out a `missing header level` (header 2 missing - straight to 3) - this could cause confusion with screenreader navigation.



