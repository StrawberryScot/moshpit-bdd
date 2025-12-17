# QE Report end of Weds 17th Dec

**Summary**

MVP looking great and working well overall and handling the majority of both basic and edge case text inputs. 

The only issue of note is the handling of formatting when it comes to white space and line breaks - bringing a disjunct of integrity between input and displayed post. Users are not currently able to use common formatting styles such as double line break spaces.


## Exploratory Test Session 1 (AM)
AM
The Test Team concurrently explored the MVP (V1) while sharing screens and making notes on shared Excalidraw doc. 

- blockers with set up/run process and readme resolved in team meeting with devs.
- interesting questions raised re artist/fan view of this page/ future elements.
- generally very impressed with clarity of layout and content structure retaining integrity with manual resizing of browser window. Also the display posts wrap intuitively.

## Manual Test Session 1 (PM)
Driver: Ben
Scribe: Kathy

We did a planned manual systematic test of MVP (V2 - now has working functionality to post a message in text format to the feed.)

### Tests Passed: ✅ 

- Single character
- Short message (1 word)
- Medium message (1 sentence)
- Longer message (paragraph)
- Message with punctuation
- Message with numbers
- Emoji
- Apostrophes and quotes
- Ampersands and symbols
- Multiple exclamation/question marks
- Parentheses and brackets
- Currency symbols
- Accented characters
- Back slashes
- HTML/XML characters
- Very long message (stress test)
- normal editability and basic navigation
- Placeholder text behavior
- copy/pasted text
- Right-to-left text (Hebrew, Arabic)


### Tests Failed/Questions raised ⚠️

- message with line breaks
- whitespace handling (internal, leading and trailing)
- do we want a character limit?

### Bugs Raised

49 
50
(both concerning whitespace and line break handling)
