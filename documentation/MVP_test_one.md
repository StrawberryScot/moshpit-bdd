# Test Notes - Manual Test ONE 

17.12.25 PM

Driver: Ben
Scribe: Kathy

Environment: Latest Zen browser (firefox variant)

## Valid Basic Inputs

**Short message (1 word)**
Test: "Hello"
Result: PASS ✅ 

**Medium message (1 sentence)**
Test: "Hello, world! This is my first post."
Result: PASS ✅ 

**Longer message (paragraph)**
Test: "We're excited to announce our upcoming tour! We'll be visiting London, Manchester, and Liverpool."
Result: PASS ✅ 

**Message with punctuation**
Test: "Hey everyone! What's up? We're back :)"
Result: PASS ✅ 

**Message with numbers**
Test: "Our album has been #1 for three weeks!"
Result: PASS ✅ 

**Message with line breaks**
Test: "line 1
line 2
line 3"
(Try pressing Enter/Return to see if it creates new lines)
Result: line 1 line 2 line 3
= FAIL ⚠️
formatting not preserved with linebreaks  


## Special Characters


**Emoji**
Test: "Hello! 🎵🎸🎤 Can't wait to see you all!"
Result: PASS ✅

**Apostrophes and quotes**
Test: "We're so excited! This is "amazing" news."
Result: PASS ✅

**Ampersands and symbols**
Test: "Rock & Roll @ The O2! See you there #concert"
Result: PASS ✅

**Multiple exclamation/question marks**
Test: "OMG!!! Are you ready??? Let's gooo!!!"
Result: PASS ✅

**Parentheses and brackets**
Test: "New album (coming soon) featuring [guest artist]!"
Result: PASS ✅

**Currency symbols**
Test: "Tickets from £10/$15/€12 available now!"
Result: PASS ✅

**Accented characters**
Test: "ÀLPHÀ met ĆHARLÏE at the CAFÉ near ÈCHO square;
ĞÜLŞEN from ÑÎMES, ØYSTEIN from ØSLO, and ŠIMON from
PRÀGUE discussed GÖDEL and ŁUKASZ over CRÊPES, 
then flew to SÃO PAULO where JOSÉ said '¡OLÁ!' to ŸVETTE and ŻUREK."
Result: PASS ✅

**Back slashes**
Test: "Check us out on Spotify\Apple Music!"
Result: PASS ✅

**HTML/XML characters**
Test: "<script>alert('test')</script>"
Test: "3 < 5 > 2"
Test: "Hello & goodbye"
(This tests for XSS vulnerability - the text should display as-is, NOT execute)
Result: PASS ✅


## Edge Cases - Length and Whitespace

**Empty submission**
Action: Click "Post" without typing anything
Expected: Error message OR button disabled OR validation prevents posting
RESULT: CAN POST EMPTY POST (nothing displayed, no space etc, just straight into hyphen then addendum)
= FAIL ⚠️ (assuming we don't want this - error message preferred...)

Also tested with empty but with 3 line-space (pressed enter). Whitespace trimmed - appears as above. Also tested with spaces as 'content' and multiple lines - also as above.

Test: 
      dwd.
  ...
..   . ..
Result: IM3
Empty line trimmed from beginning and start of second line - ie display starts directly with dwd. Then, line breaks/empty space is displayed as single space.

Test: IM4
Result: IM5
= FAIL ⚠️


**Multiple spaces between words**
Test: "Hello     world     with     multiple     spaces"
Result: Hello world with multiple spaces
= ! Truncates multiple spaces in text as well as leading and trailing spaces
= FAIL ⚠️

**Single character**
Test: "A"
RESULT: PASS ✅

**Very long message (stress test)**
Copy/paste v long paragraph (500+ words)

Test: 1930 characters (includes 47 line breaks)
RESULT: PASS - text posted as expected (with line break considerations as revealed in tests below. Display shows the whole message 
! No truncation/scroll) ✅

Test: 38,600 characters. As above. ✅

⚠️ NB do we want a character limit?


## Formatting

**Can you edit after typing but before posting?**
Action: Type, delete some, type more - does it work smoothly?
Result: PASS ✅

**What happens if you click outside the box?**
Action: Click elsewhere - does content save as draft or disappear?
Result: text remains in editor. Box focus blue outline disappears and reappears when click back in, with text intact. ✅

**Can you use keyboard shortcuts?**
Action: Try Ctrl+A (select all), Ctrl+C/V (copy/paste), Ctrl+Z (undo)
Test: copy paste undo redo 
Result: Pass ✅
(NB enter does not post) ⚠️

**Placeholder text behavior**
Check: Does "Share an update with your fans..." disappear when you click in?
Check: Does it reappear if you clear the field?
Result: Does not disappear until you start typing. Reappears when box blank. ✅ 

**Cursor position**
Check: Click in middle of text - can you edit there?
Result: PASS ✅

**Tab characters (if possible to input)**
Test: "Hello        World" (with tab between)
Result: Tab just takes focus to Post button.


## Copy/Paste & Input Methods

**Copy/pasted text from Word/Google Docs**
Check: Does it preserve or strip formatting?
Result: Does not preserve formatting as tested: bold, italic, font
NB does truncate whitespace formatting as noted. ⚠️

**Copy/pasted text with emojis**
Test: Copy "Hello 👋🌟💫" from another source
Result: PASS ✅

**Right-to-left text**
Test: "مرحبا" (Arabic) or "שלום" (Hebrew)
Result: PASS ✅







