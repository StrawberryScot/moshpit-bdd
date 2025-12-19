# Moshpit - Functional Specification
Draft 1 (19.12.25)

## Authentication & Accounts

| Id | Item | Status |
| --- | --- | --- |
| AA001 | New user can sign up with email and password |  |
| AA002 | Signed up users can create an account with name, username, location and bio |  |
| AA003 | Fan accounts and associated data belong to specific signed up users |  |
| AA004 | Signed up users can log in if providing correct credentials |  |
| AA005 | Logged in users can log out |  |
| AA006 | Passwords are not stored in plain text `CHECK`|  |
| AA007 | Fan account pages are accessible to logged in users, and logged out users (public)|  |
| AA008 | Follow artist function only accessible to logged in users |  |
| AA009 | Artists can create an Artist Page with name, genre, bio, and Spotify authentication |  |

## Design

| Id | Item | Status |
| --- | --- | --- |
| DE001 | Sign Up and Create Profile pages have clear input validity instructions |  |
| DE002 | Logged in users arrive on personalised Fan Feed Page |
| DE003 | Navigation bar accessible from all pages |  |
| DE004 | Navigation bar allows immediate access to all the main pages |  |
| DE005 | Fan profile page showing associated fan data (if logged in) |  |
| DE006 | List on fan profile showing a user's followed artists (if logged in) |  |
| DE007 | Individual Artist pages including name, genre, bio, concert dates and message feed |  |
| DE008 | Individual Concert pages that can be accessed through Artist page or search `CHECK`|  |
| DE009 | Search bar with drop down filtering `CHECK AND ADD TO THIS` |  | 
| DE009 | Logged in users can log out from all pages |  |
| DE0010 | Logged out users can log in from Sign In/Sign Up page |  |


## Fan Profile Page

| Id | Item | Status |
| --- | --- | --- |
| FP001 | Fan Profile Page displays fan name, username |  |
| FP002 | Fan Profile Page displays bio, profile picture if user has uploaded |  |
| FP003 | Users can link their Spotify to their fan page `add what data visible` |  |
| FP004 | User's top 5 Spotify artists are displayed on their fan page |  |
| FP005 | Users can see suggestions of artists to follow based on Spotify API |  |
| FP006 | Logged in users can unfollow artists from followed artist list on their fan page |  | 
| FP007 | Users can search/filter their followed artist list `TBD`|  |


## Fan Feed

| Id | Item | Status |
| --- | --- | --- |
| FF001 | Fan Feed displays posts from user's followed artists in chronological order (newest at top) |  |
| FF002 | User can click through to artist page from posts on Fan Feed |  | 
| FF003 | User can click through to concert page from concert dates on Fan Feed |  | 
| FF004 | User sees 'Follow artists to see updates' messages if feed empty (ie no follows) |  | 

## Artist Page

| Id | Item | Status |
| --- | --- | --- |
| AR001 | Artist can create a page which displays name, genre, bio, concert dates and message feed |  |
| AR002 | Artist can edit personal information on artist page |  |
| AR003 | Artist can post a text format message to their updates feed |  |
| AR004 | Artist can post an image format message to their updates feed |  |
| AR005 | Artist can post a tour date post to their updates feed |  |
| AR006 | Artist can edit and delete a tour date or message |  |
| AR007 | Artist can post multiple messages to their updates feed |  |
| AR008 | Artist can post multiple tour dates to their updates feed |  |
| AR009 | Tour dates posted by artist are displayed as list on artist page |  |
| AR010 | Artist only sees prompt to create a post if empty state |  |
| AR011 | Artist can link Spotify to their artist page `add what data visible` |  |
| AR012 | Spotify web player allows user to play relevant music while on page |  |
| AR013 | Artist pages are publically visible |  |
| AR014 | Logged in users can follow artists from individual artist page |  |
| AR015 | Logged in users can unfollow artists from individual artist page |  |
| AR016 | Button on artist page changes state between follow and unfollow |  |
| AR017 | Follower count displayed on artist page |  |


## Search Page


## Concert Page

| Id | Item | Status |
| --- | --- | --- |
| CO001 | Concerts can be clicked on artist page and lead to associated individual concert page |  |
| CO002 | Individual concert pages display title, band, location, date and description |  |
| CO003 | Fans can upload images with captions to individual concert page |  |
| CO004 | Users see 'Be the first to share memories!' message if no fan content |  |

## API

| Id | Item | Status |
| --- | --- | --- |
| AP001 | Root level /api resource, explaining basic usage |  |
| AP002 | Sub-level resource types can be specified by name |  |
| AP003 | Sub-level resource types: `FILL IN AS APPROPRIATE eg concerts, bands, accounts` |  |
| AP004 | Subset of resources of type concert can be returned via date and location filters `AMEND AS NECCESSARY`|  |
| AP005 | Individual resources of a specific type can be specified by name or id (type dependent) |  |


## Accessibility & Maintenance

| Id | Item | Status |
| --- | --- | --- |
| AC001 | Product is keyboard navigable 
| AC002 | Elements are clearly labelled with IDs 
| AC003 | Error messages are helpful and provide clear re-route action
| AC004 | Interface has clear colour contrast and is readable
| AC005 | Alt text descriptions present and clear


## Other

| Id | Item | Status |
| --- | --- | --- |
| OT001 | All dates in European (DMY) format: DD/MM/YYYY |  |
| OT002 | Setup instructions for running the server locally |  |
| OT003 | Chrome Desktop support only, minimum resolution 1280 × 1024 |  |