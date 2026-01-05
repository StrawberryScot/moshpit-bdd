### Spotify OAuth Integration Issue Log
Mon Jan 5 2026
Kathy Peacock

**Initial Problem:** "Oops! Something went wrong" error on Spotify login page

![spotify API error message 1](/issues%20logs%20and%20resources/screenshots_spotify_api_issues/spotify_error_1.png)

**Root Cause:** Redirect URI mismatch between application.yml and active localhost server.


**Testing Notes:**
- Spotify OAuth is extremely strict about redirect URI matching
- `localhost` and `127.0.0.1` are treated as different domains
- Server restart required after yml changes

- ACTION: accessed application through the 127 route outlined in the spotify section of application.yml - this then meant I was able to successfully log in to Spotify on the Spotify API redirect page, however I then ended up with error pages. 

- ERROR PAGES. 

![Whitelabel error page 1](/issues%20logs%20and%20resources/screenshots_spotify_api_issues/spotify_error_message_spotifyConnected=true.png)

![Whitelabel error page 2](/issues%20logs%20and%20resources/screenshots_spotify_api_issues/spotify_error_message_state_mismatch.png)


## Bug Description
After successfully authenticating with Spotify and being redirected back to the application, a 500 Internal Server Error occurs.

## Steps to Reproduce
1. Navigate to user profile page
2. Click "Link Spotify Account" button
3. Enter Spotify credentials and authorize
4. Spotify redirects to callback URL with auth code
5. **Expected:** User returned to profile with Spotify linked
6. **Actual:** Whitelabel Error Page with 500 Internal Server Error

## Error Details
- **URL:** `127.0.0.1:8080/user?spotifyConnected=true`
- **Error Type:** Internal Server Error
- **Status Code:** 500
- **Timestamp:** Mon Jan 05 14:27:34 CET 2026
- **Error Message:** "This application has no explicit mapping for /error, so you are seeing this as a fallback."

## Environment
- Browser: Chrome
- Server: (127.0.0.1:8080)
- User: test user (Kathy Test)

## Expected Behavior
After Spotify OAuth completes:
1. User should be redirected to their profile page
2. Spotify connection status should display
3. Spotify data should be visible (top artists, etc.)

## Impact
- **Severity:** Critical
- **Blocks:** Spotify integration testing
- **User Journey:** Fan/Artist linking Spotify account

## Additional Notes
- Spotify authentication itself works (when I manually navigated back to my user page, the 'Connect your Spotify' button had changed to 'Disconnect Spotify' - plus, the url stated `spotifyConnected=true`)

![User page after Spotify connection](/issues%20logs%20and%20resources/screenshots_spotify_api_issues/user_page_spotify_connected_no_display.png)

NB no Spotify data shown.

- Issue is in callback processing/token exchange
- No custom error page configured (showing Whitelabel)

## Next Steps Needed
- Check server logs for stack trace
- Verify Spotify token exchange logic
- Suggest devs add error handling for OAuth callback failures


- ACTION: looked at server log stack trace in terminal, which displayed the following:

![server log stack trace data](/issues%20logs%20and%20resources/screenshots_spotify_api_issues/server_stack_trace.png)


**Status:** Blocked by 500 error after callback

**Testing Progress:**
1. ✅ Resolved redirect URI configuration (localhost vs 127.0.0.1)
2. ✅ Successfully authenticated with Spotify
3. ❌ 500 Internal Server Error on callback processing


**Technical Details:**
- Spotify OAuth flow works up to callback
- Backend fails to process auth code exchange
- No custom error handling implemented
- Query param `spotifyConnected=true` suggests partial success

**Blocked Testing:**
- Spotify data display verification
- Unlink functionality
- Re-authorization flow
- Persistence after logout

**Workaround:** None - requires backend fix

**Questions for Devs:**
    - Is token exchange logic implemented?
    - What exact Spotify data should display after successful link?

**Demo Day Note:**
Can showcase OAuth flow troubleshooting:
- Identified and resolved redirect URI mismatch
- Successfully completed Spotify authentication
- Identified 500 error in callback processing
- Documented clear reproduction steps for devs