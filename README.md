# Quality Engineering Final Project
**Makers Software Engineering (QE) Bootcamp**

**Quality Engineering Team:** Benjamin Loveday & Kathy Peacock  
**Project Duration:** 2 weeks      
**Demo Day:** 09 January 2025

This Project was the culmination of our 14 week Software Engineering (QE specialism) Bootcamp with Makers. This intensive training experience was the start of our Software Testing Apprenticeship with Universal Music Publishing Group, UK - Global Technology Department.

---

## README Contents
- [Project Overview](#project-overview)
- [Our Role as Quality Engineers](#our-role-as-quality-engineers)
- [Technical Tools & Stack](#technical-tools--stack)
- [Key Contributions](#key-contributions)
- [Testing Approach](#testing-approach)
- [Key Learnings](#key-learnings)
- [Standout Achievements](#standout-achievements)

---

## 🎵 Project Overview

**Moshpit** is a music platform designed to connect fans with artists, enabling artists to share updates, tour dates, and content while fans can follow their favorite artists and stay updated on concerts and news - as well as displaying dynamic Spotify data, such as a user's Top 5 Artists, and 'currently listening' widget (Spotify API integration).

### The Challenge
This was a **greenfield project** built from scratch with:
- No existing user requirements or specifications
- A development team unfamiliar with formal specification documentation and no previous experience of working with QEs.
- No project manager, BA, or PO roles
- Very short timeline (8 days from conception to demo product feature freeze...)
- Ongoing team uncertainty around feature scope and implementation details

### The Product
A full-stack web application featuring:
- Fan and Artist authentication & profiles
- Artist pages with bios, genres, and Spotify integration
- 'Suggested' content based on Spotify data
- Concert listings and event pages
- Post feeds (text and image updates)
- Follow/unfollow functionality
- Filterable search capabilities
- Fan-generated dynamic content (concert photo galleries)

---

## 👾 Our Role as Quality Engineers

As the dedicated QE team, we positioned ourselves as **strategic partners in product development** rather than reactive bug-finders.

### Core Responsibilities
- **Requirements Engineering:** Transformed vague concepts into formal specifications
- **Test Strategy:** Designed comprehensive testing approaches across manual, automated, and accessibility domains
- **Process Improvement:** Established communication standards, documentation practices, and workflow optimisation
- **Technical Testing:** Exploratory, boundary, equivalence partitioning, API, accessibility, static analysis and test data generation.
- **Stakeholder Communication:** Clear, concise reporting through GitHub Issues and daily updates

---

## 🛠️ Technical Tools & Stack

### Programming & Automation
- **Python** - Test data generation, automation scripting
- **Java** - BDD test implementation
- **Selenium WebDriver** - Browser automation
- **Cucumber & Gherkin** - BDD scenarios and step definitions

### Test Data Generation
- **Faker v10.2.0** - Internationalized test data (28+ locales)
- **Pillow (Python Imaging Library)** - Custom image generation for upload testing
- **Custom Scripts** - CSV generation, locale-specific data

### Database & API Testing
- **TablePlus** - Database inspection and manual data manipulation
- **PostgreSQL** - Backend database
- **Postman** - API endpoint testing
- **cURL** - Command-line HTTP requests

### Accessibility Testing
- **Colorblindly** - Colour contrast simulation
- **WAVE** - Web accessibility evaluation
- **Lighthouse** - Performance and accessibility auditing
- **Apple VoiceOver** - Screen reader testing

### Static Analysis
- **SonarQube** - Code quality, security, maintainability analysis
- **Chrome DevTools** - Network analysis, performance profiling
- **Pylint** - Python code quality

### IDE & Package Management
- **IntelliJ IDEA** - Primary development environment
- **VS Code** - Secondary editor for scripts and documentation
- **Homebrew** - Package management

### Project Management & Communication
- **GitHub** - Issues tracking, test repository, version control
- **Slack** - Quick questions, team coordination
- **Zoom** - Pair programming, team meetings
- **Excalidraw** - Visual documentation, collaborative diagramming and test planning

---

## 💡 Key Contributions

### 1. Specification Creation
**The Problem:** Developers had no formal specification and were uncertain about MVP scope.

**Our Solution:**
- Created a comprehensive **"Spec Questions Document"** covering expected user actions, functionality, display, and UX details for developer input
- Organised questions by Page and annotated for Artist/Fan distinctions
- Facilitated team discussion to answer each question methodically
- Drafted **formal Functional Specification** with clear feature IDs, items, and status tracking

**Impact:**
- Enabled developers to make informed implementation decisions
- Created testable requirements with clear acceptance criteria
- Established a "Yes, No, Not Yet" framework for feature prioritisation and implementation roadmap
- Reduced ambiguity and back-and-forth during development

**Documentation:** `Product_Specification.md` 

---

### 2. Behavior-Driven Development Advocacy
**Our Approach:**
- Introduced BDD methodology to align development with user needs
- Created initial `.feature` files with Gherkin scenarios
- Implemented step definitions in Java
- Demonstrated value of starting with purpose rather than implementation

**Why It Mattered:**
- Helped developers understand *why* features exist, not just *what* to build
- Made features more testable from the start
- Brought testers into the planning cycle early
- Created living documentation that serves as regression tests

---

### 3. Accessibility Advocacy
**From Day 1, we positioned accessibility as a core feature, not an afterthought.**

**Activities:**
- Shared WCAG 2.1 resources and "Designing with Accessibility in Mind" guides
- Emphasised accessibility benefits for the entire team, not just end user
- Pushed for meaningful HTML element IDs for both accessibility and test automation
- Negotiated styling decisions to ensure UX and accessibility weren't left to the last minute

**Testing Coverage:**
- **Keyboard navigation:** Tab order, focus indicators, Enter/Escape functionality
- **Screen reader compatibility:** Element labelling, ARIA attributes, alt text
- **Color contrast:** WCAG AA compliance using Colorblindly and WAVE
- **Visual clarity:** Link states, button toggle indicators, empty state messaging

**Impact:**
- Multiple accessibility bugs fixed during development
- Developers gained awareness of accessible design patterns
- Created a culture of team accessibility consideration throughout the project

---

### 4. Test Data Generation

#### Text Data - Internationalisation (i18n) Testing
**Problem:** Need to test with realistic, diverse user data across multiple languages and character sets.

**Solution:**
- Built Python script using Faker v10.2.0
- Generated 300+ user profiles across **28 locales** 
- UTF-8 character support (Cyrillic, Japanese, Arabic)
- Right-to-left (RTL) text handling
- Locale-specific formatting (dates, currency)
- Created customised matched city/country pairs per locale in CSV format

**Bug Discovery During Generation:**
We found a bug **in Faker itself**:
- Lithuanian locale (`lt_LT`) generated names in format: `"Surname, Firstname"`
- This is NOT a valid Lithuanian naming convention (should be `Firstname Lastname`)
- The hardcoded comma broke our CSV parsing
- Investigated Faker source code to confirm root cause

**Learning takeaway:** Always validate (even establised) test data generators against real-world conventions and bugs.

#### Image Data - Profile Picture & Media Upload Testing
**Challenge:** Test image upload functionality across various file sizes, resolutions, and formats.

**Solution:**
- Built Python script using **Pillow (PIL)** library
- Generated **15+ test images** with precise control:
  - Resolutions: 1x1 to 8000x8000 pixels
  - Formats: JPG, PNG
  - Aspect ratios: Square and non-square (1920x1080, 1080x1920, 100x1000)
  - File sizes: 0.07KB to 495KB

**Test Image Categories:**
1. **Valid standard sizes:** 50x50, 200x200, 500x500, 800x800, 1500x1500, 2000x2000
2. **Edge case tiny:** 1x1, 10x10 (minimum size handling)
3. **Edge case huge:** 5000x5000, 8000x8000 (maximum size/memory handling)
4. **Non-square:** Testing cropping/scaling logic

**Comparison with Faker Image Download:**
- Also attempted to use Faker's `image_url()` to download realistic profile pictures
- Result: Partially successful - many URLs returned generic placeholders or failed
- Conclusion: PIL-generated images provided superior, predictable test coverage

**Impact:**
- Comprehensive image upload testing across edge cases
- Discovered UX inconsistency in image handling
- Created reusable test image library for future testing

**Documentation:** `test_images/` directory + Python generation scripts for both text and image

---

### 5. Exploratory Testing
**Methodology:**
- **Black box approach:** No code review before testing (fresh user-focussed perspective)
- **Timeboxed sessions:** 1-hour focused explorations
- **Boundary value analysis:** Testing at/around limits (e.g., 499, 500, 501 characters)
- **Equivalence partitioning:** Categorising test cases to avoid repetition

**Test Categories:**
- **Special characters:** Emojis, apostrophes, quotes, accents, symbols
- **Edge cases:** Empty submissions, very long inputs (1000+ characters), whitespace-only
- **International characters:** Accented (café, ALPHA, CHARLIE), Cyrillic (Москва), non-Latin scripts (日本, العربية)
- **Security:** XSS attempts (`<script>alert('XSS')</script>`), SQL injection (`'; DROP TABLE users;--`), HTML injection

**Notable Findings:**
- **Empty post submission FAIL:** Could post empty content (no validation), resulting in hyphen-only display
- **XSS vulnerability:** HTML/XML characters not properly escaped - `<script>` tags displayed as-is rather than executing (PASS, but needed verification)
- **Line break handling:** Multiple consecutive whitespace characters collapsed to single space
- **Character limits:** No enforcement on bio field - 10,000+ character bios accepted

**Documentation:** Detailed exploratory test results in testing journal

---

### 6. API Troubleshooting
**The Problem:** Spotify OAuth integration caused 500 Internal Server Error after successful authentication.

**Our Investigation Process:**

1. **Terminal Log Analysis**
   - Captured server logs showing error at callback processing
   - Identified `Internal Server Error (type=Internal Server Error, status=500)`

2. **Browser DevTools Network Tab**
   - Monitored HTTP requests during OAuth flow
   - Verified Spotify redirect URL mismatch: `localhost` vs `127.0.0.1`
   - Observed request/response cycle breakdown at token exchange

3. **Postman & cURL Testing**
   - Isolated API endpoint testing
   - Sent modified requests to debug callback handling
   - Validated Spotify API credentials and token exchange logic

4. **Database Inspection (TablePlus)**
   - Manually adjusted data to test persistence
   - Verified OAuth token storage expectations

**Bug Identified & Documented:**
- Redirect URI configuration mismatch between `application.yml` and Spotify Developer Dashboard
- Backend callback processing failure at token exchange
- No custom error handling (Whitelabel error page)

**New Skills Acquired:**
- **Route discovery:** Used grep to locate API endpoints in codebase
- **Network debugging:** HTTP request/response analysis
- **Command-line tools:** `find`, `grep`, `more` for codebase scanning

---

### 7. Static Testing
**Tool:** SonarQube

**Analysis Areas:**
- **Security:** Vulnerability detection
- **Reliability:** Bug-prone code patterns
- **Maintainability:** Code complexity, duplication

**Key Finding:**
- `PostsController.java` flagged for **high cognitive complexity (25)**
- Recommendation: Refactor method to reduce complexity to ≤15
- Deeply nested if-else blocks identified as difficult to understand, maintain, and modify

**Our Approach:**
- Raised as enhancement suggestion rather than critical bug
- Prioritised based on development velocity (not blocking MVP)
- Documented for hypothetical future refactoring

---

### 8. Process Improvements
**Challenges We Identified:**

**1. Lack of Dedicated Roles**
- No Project Manager → Meetings were unfocused, ticket allocation unclear
- No BA/PO → Requirements gathering fell entirely on QE team
- No clear Definition of Done

**2. Bug Tracking Visibility**
- Our bug tickets were lost in the developer-created Kanban board
- No visual distinction between bugs, features, and enhancements

**Solutions We Implemented:**

**GitHub Issue Management:**
- Created custom labels: `bug`, `enhancement`, `core-functionality`, `readability/accessibility`, `regression`
- Implemented colour-coding for visual separation
- Made issues easily filterable and sortable

**Standardised Bug Report Template:**

**Communication Standards:**
- Established git branch naming conventions: `feature/`, `bugfix/`, `test/`
- Commit message format: `[CATEGORY]: Brief description`
- Slack channels for different purposes (quick questions vs. meeting planning)

**Workflow Optimisation:**
- Advocated for **iterative development** over premature optimization
- Reduced non-value-gaining time in group meetings
- Encouraged "document as you go" approach

---

## 🔍 Testing Approach

### Test Techniques Applied

| Technique | Purpose | Example |
|-----------|---------|---------|
| **Black Box Testing** | Fresh perspective, no code bias | Initial MVP exploratory test, i18n and image testing |
| **Boundary Value Analysis** | Find edge case bugs at limits | Testing character limits: 499, 500, 501 |
| **Equivalence Partitioning** | Avoid redundant testing | Categorising inputs: valid/invalid/edge |
| **Exploratory Testing** | Uncover unexpected behaviors | Special characters, emoji, user journeys |
| **Decision Tables** | Systematic scenario coverage | User authentication: logged in/out × fan/artist |
| **Static Analysis** | Code quality without execution | SonarQube cognitive complexity check |
| **API Testing** | Backend validation | Postman endpoint testing, cURL debugging |
| **Accessibility Testing** | WCAG 2.1 compliance | Keyboard nav, screen readers, colour contrast |

---

## 🌟 Standout Achievements

### 1. Finding Our Footing as new QEs from Different Backgrounds

**Diverse perspectives enriched the team**
- We brought **user empathy** and **real-world perspective** that purely technical teams sometimes lack
- Advocated for users in ways developers might not have considered
- Bridged communication gaps between technical and non-technical stakeholders
- Demonstrated that QE is not just about technical skills—it's about critical thinking, curiosity, and empathy

---

### 2. Digging deeper into Representative Test Data, Bias Activism, & AI Ethics
**Our Approach:**
- Generated test data across **28 locales** to ensure internationalization support
- Actively considered **cultural representation** in our test scenarios and further learned how diverse test data catches bugs that homogeneous data misses
- Researched and raised questions about **algorithmic, AI and data bias** 

---

### 3. Championing Accessibility Across the Whole SDLC Lifecycle
**From Day 1 to Day 10:**

- Multiple accessibility bugs fixed **during development** (not as post-launch fixes)
- Developers gained awareness and skills they'll carry to future projects
- Created a culture where accessibility is a feature (in our team as well as product), not an afterthought

---

### 4. Having Fun Coding Data-Generation Scripts
**The Joy of Scripting:**
- Writing Python scripts to generate 300+ user profiles felt like creative problem-solving
- Building image generation with Pillow gave us precise control over test scenarios
- Discovering bugs in Faker itself was an enjoyable "meta-bug" moment

---

### 5. Newfound Confidence - Exercising Technical Independence

- Practiced and built upon wide-ranging technical skills and theory from Bootcamp
- Independently troubleshot Spotify OAuth 500 errors using logs, DevTools, Postman, and database inspection
- Learned command-line tools (grep, curl) on the fly
- Used SonarQube to analyse code quality with confidence
- Gained confidence communicating with developers and stakeholders - both technically and in advocating for the value of the tester's perspective from day 1, and for mutual support to be able to bring the most QE impact to our team.

---

## 📊 Project Artifacts

### Documentation Delivered
- **Product Specification (Draft 1):** Formal functional spec with feature IDs and status tracking
- **Testing Journal:** Day-by-day log of activities, findings, and learnings
- **BDD Test Repository:** Cucumber feature files and Java step definitions
- **Bug Reports:** Detailed GitHub Issues with reproduction steps, screenshots, and severity labels
- **Test Data:** 300+ internationalised user profiles (CSV), 15+ image test cases
- **Process Documentation:** Git conventions, commit standards, bug report template
