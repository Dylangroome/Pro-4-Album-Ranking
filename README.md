# Album Review

## Author
Dylan Groome

## Project Overview
*  The Album Review is a place for discussion about the most influential rap albums. Each album post is dedicated to a popular artist , with a detailed description. 
* You can view the deployed website [here]https://pro-4-album-ranking.herokuapp.com/).

<img width="1439" alt="Screenshot 2023-04-30 at 07 34 18" src="https://user-images.githubusercontent.com/108524172/235340480-0bb17896-907f-4670-bcbd-64f7794ea745.png">


## TABLE OF CONTENTS
- [STEM & LEAF - A PLANT CARE SPACE FOR BEGINNERS](#stem---leaf---a-plant-care-space-for-beginners)
  * [Author](#author)
  * [Project Overview](#project-overview)
  * [UX](#ux)
    + [Project Goal](#project-goal)
    + [User Stories](#user-stories)
  * [DESIGN CHOICES](#design-choices)
    + [Colors](#colors)
    + [Typography](#typography)
    + [Images/Icons](#images-icons)
    + [Animations](#animations)
    + [Responsiveness](#responsiveness)
  * [WIREFRAMES](#wireframes)
    + [Post List](#post-list)
    + [Post Detail](#post-detail)
  * [FEATURES/STRUCTURE](#features-structure)
    + [Navigation](#navigation)
    + [Plant List](#plant-list)
    + [Plant Detail](#plant-detail)
    + [Likes](#likes)
    + [Comments](#comments)
    + [Register](#register)
    + [Login/Logout](#login-logout)
    + [Footer](#footer)
    + [Error 404/403/500](#error-404-403-500)
    + [Features for Future Development](#features-for-future-development)
  * [DATA MODEL](#data-model)
  * [TESTING](#testing)
    + [Validation Testing](#validation-testing)
    + [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
    + [Manual Testing](#manual-testing)
    + [Automatic Testing](#automatic-testing)
    + [Outstanding Defects](#outstanding-defects)
    + [Defects of Note](#defects-of-note)
  * [ACCESSIBILITY](#accessibility)
    + [Lighthouse Audit](#lighthouse-audit)
    + [Keyboard Navigation](#keyboard-navigation)
  * [TECHNOLOGIES USED](#technologies-used)
  * [DEPLOYMENT](#deployment)
  * [CREDITS](#credits)
    + [Media](#media)
  * [ACKNOWLEDGEMENTS](#acknowledgements)

## UX

### Project Goal
* The aim of the project is to provide a friendly informative interactive space  about popular artists most influential works and to allow for conversation and sharing of experiences of them.

## Agile Methodology

An Agile approach to creating this app has been applied. Githubs projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience.


By using AGILE methodology in this project I was able to deliver a site which had all required functionality and was able to give even more extra detail when going through the project.

I used GitHub projects board to create the user stories and keep track of my tasks.

### User Stories
* 
* https://github.com/users/Dylangroome/projects/9/views/1
* 
 
## DESIGN CHOICES

### Colors

<img width="9" alt="Screenshot 2023-04-30 at 07 34 06" src="https://user-images.githubusercontent.com/108524172/235340607-ebbbbce8-c465-413d-857f-649fcd6f1a07.png">

 
- A plain white is used for ease of navigation and to highlight kee elements like the album’s. 
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.

<img width="308" alt="Screenshot 2023-04-30 at 07 41 39" src="https://user-images.githubusercontent.com/108524172/235340692-f9f176a2-f719-468d-91e7-bc083e190b3e.png">


### Typography

<img width="773" alt="Screenshot 2023-04-30 at 07 49 31" src="https://user-images.githubusercontent.com/108524172/235340730-65c202b4-e1c8-408c-bc64-355e7ae6c0d0.png">

- The font fst-italic [here](https://bootstrapshuffle.com/classes/typography/fst-italic).

- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

### Images/Icons

<img width="319" alt="Screenshot 2023-04-30 at 07 53 50" src="https://user-images.githubusercontent.com/108524172/235340817-65b96128-ed69-409a-beed-e5f94be1d8a3.png">


- The icons were chosen to provide clear understanding of each album.
- Each summary has the same information structure with all icons standard throughout the site.

### Animations

### Responsiveness

- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## WIREFRAMES

### Post List
- The post list page was designed using cards to show a quick summary of each plant.
- The user can click and find out more about a plant that interests them.
<img width="636" alt="image" src="https://user-images.githubusercontent.com/97494262/209437372-83b2bc1e-68a0-4a75-8e86-d78b69df4a7d.png">

### Post Detail
- Each blog post provides detail about the plant and a list of instructions to care for it. 
- The registered user can also comment and like the post if desired.
<img width="611" alt="image" src="https://user-images.githubusercontent.com/97494262/209437385-b8be9fe9-bbbb-4110-a9af-e0f5239f3cc9.png">

## FEATURES/STRUCTURE

### Navigation
- The users will have a choice of home, login/logout & register when visiting the site. 
- There is a subtle hover state on each of the navigation items for better user experience.
- For mobile devices, the navigation toggles to a hamburger menu.

### Album List
- The users will have a list of albums with a title, excerpt and detailed info for each album.
- The image and title are linked, so users may click on either and be taken to the album detail page.
- There is a hover state on the title to show the user they can click on the post.

<img width="390" alt="Screenshot 2023-04-30 at 07 58 15" src="https://user-images.githubusercontent.com/108524172/235340998-9f26887a-d73e-45e2-b3fc-af156613bef9.png">


### Artist’s Detail
- Each post has a short article about the artist information in detail.
- The structure of each post is consistent. 

<img width="725" alt="Screenshot 2023-04-30 at 08 23 38" src="https://user-images.githubusercontent.com/108524172/235341062-45adae13-4e99-469b-bd71-d186bc39e044.png">


### Likes
- If the user is logged in, they will be able to add a like:

<img width="170" alt="Screenshot 2023-04-30 at 08 28 07" src="https://user-images.githubusercontent.com/108524172/235341263-dc28d642-8cb9-420f-b390-fe400414cba8.png">


- The user is able to easily return to the home page using the go back button or clicking the logo at the top of the page.

### Comments
- If a post doesn't have any comments, the user will see the below if not logged in:

<img width="653" alt="Screenshot 2023-04-30 at 08 29 12" src="https://user-images.githubusercontent.com/108524172/235341304-1c7e8141-587c-4c1a-a5fd-3adb943b60a8.png">


- If logged in, users will be encouraged to share their experience:

<img width="1001" alt="Screenshot 2023-04-30 at 08 30 01" src="https://user-images.githubusercontent.com/108524172/235341342-7febdfb1-23b9-4d09-b11f-60eb8412c244.png">



- The user will be able to edit their comment using a form.


- The user will be able to delete their comment:


### Register 
- The user will be able to easily sign up as a user using the below form.
- If users are already registered, there is a link to easily navigate to login instead

<img width="476" alt="Screenshot 2023-04-30 at 08 35 33" src="https://user-images.githubusercontent.com/108524172/235341505-395f68fe-20ca-424f-b2ab-676a1452c640.png">


### Login/Logout 
- The users can easily sign in using the below form with an option to 'remember me' if desired.
- If a user hasn't registered, there is a link to easily navigate to sign up instead.

<img width="650" alt="Screenshot 2023-04-30 at 08 36 23" src="https://user-images.githubusercontent.com/108524172/235341533-ed85a52d-b991-438e-98a0-94f7481c0758.png">


### Footer

<img width="1029" alt="Screenshot 2023-04-30 at 08 38 30" src="https://user-images.githubusercontent.com/108524172/235341590-abe2f33b-cfe0-4ea5-bf9e-fb08e07f16de.png">


### Error 404/403/500
- There are error pages in place in case a user is taken to a restricted area or the page doesn't exist.
- The return home button will take the user back to the plant list page.

<img width="1035" alt="Screenshot 2023-04-30 at 08 39 02" src="https://user-images.githubusercontent.com/108524172/235341614-5f94100b-2ce3-430d-aff4-02778a8073c4.png">


### Features for Future Development
- A details page for each song of the albums
- a side by side album comparison for ranking 
- a global leaderboard of the highest rated albums
- more artist detail pages 
- more albums

## DATA MODEL


- [X] C - Site users can create/register their own profile to interact with the album posts.
- [X] R - Site users can open and read the album blog posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a album detail post.
- [X] D - Site users can eliminate their like and comment if desired on a album detail post.


* ### Album
This data model is used to store all the relevant information about albums:

| Field       | Data Type         | Purpose                          | Form Validation                  |
|-------------|-------------------|----------------------------------|----------------------------------|
| pk          | unique Identifier |                                  |                                  |
| title       | CharField         | Album Nmae                       | required, max length 200, unique |
| year        | CharField         | Album Year                       | max_length=25, blank=True        |
| Rated       | CharField         | Album rateing                    | max_length=10, blank=True        |
| released    | CharField         | Album release                    | max_length=25, blank=True        |
| slug        | SlugField         | Urls                             | required, unique                 |
| content     | textfield         | for text                         |                 |
| artist      | ManyToManyField   | link to artist                   | Artist, blank=True               |
| genre       | IntegerField      | music genre                      | choices=GENRE_CHOICES, default=1 |
| featured_image   | CloudinaryField   | To store logo               | image', default='placeholder'    |
| excerpt     | TextField         | Business summary                 | not required                     |
| created_on  | DateTimeField     | Timestamp of the creation        | automatic                        |
| status      | IntegerField      | Draft vs Published               | required, default is Draft       |


* ### Artist
This data model is used to store all the relevant information about artist:

| Field       | Data Type         | Purpose                          | Form Validation                  |
|-------------|-------------------|----------------------------------|----------------------------------|
| pk          | unique Identifier |                                  |                                  |
| title       | CharField         | Album Nmae                       | required, max length 70, unique  |
| slug        | SlugField         | Urls                             | required, unique                 |
| piece       | textfield         | for text                         |                                  |
| featured_image   | CloudinaryField   | To store logo               | image', default='placeholder'    |


- [X] C - Site users can create their own comments using a form on each album post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

* ### Comment
This data model is used to store the comments of the users along with their sentiments:

| Field       | Data Type         | Purpose                                  | Form Validation                  |
|-------------|-------------------|------------------------------------------|----------------------------------|
| pk          | unique Identifier |                                          |                                  |
| album       | ForeignKey        | One to many relation w/Album             | required but automatic           |
| name        | CharField         | To be shown below comment                | required but automatic           |
| email       | EmailField        | To be stored in database                 | required but automatic           |
| body        | TextField         | To be shown, it is the comment           | required                         |
| created_on  | DateTimeField     | To be shown below the comment            | required but automatic           |
| approved    | BooleanField      | To let admin approve before publishing   | required, auto is False (*)      |
| rate        | CharField         | To express the rateing                   | required, default is 7           |

(*) Please notice that in the current version and for better interactivity for the users, not yet approved comments are also shown on the site.

# Testing

## Lighthouse
The application has been tested with Chrome Dev Tools Lighthouse Testing which tests the application for:

* Performance
* Accessibility
* Best Practices
* SEO

### Home Page
![Home page]<img width="652" alt="Screenshot 2023-04-30 at 09 33 38" src="https://user-images.githubusercontent.com/108524172/235343675-d49cf29b-b2f0-4c41-9be9-35b612ba0638.png">


### Album Page
![Album page]<img width="592" alt="Screenshot 2023-04-30 at 09 38 26" src="https://user-images.githubusercontent.com/108524172/235343945-4817cf6c-e400-4b15-895d-15301df6f490.png">


### Artist Page
![Artist](

### Account Page
![Account]

## HTML Validator

When running my HTML code through the [HTML Validation service](https://validator.w3.org/), I encountered a few minor errors that have now all be corrected.

This is the home page -

![HTML error index page](static/readme/escaperoom-html1.jpg)

Fixed

![Home page fix](static/readme/html-test1.jpg)

This is the rooms page -

![HTML room page](static/readme/escaperoom-html2.jpg)

Fixed

![Room page fix](static/readme/html-test2.jpg)

This is the booking page

![Booking page](static/readme/html-test3.jpg)

This is the account with booking page

![Account with booking](static/readme/html-test4.jpg)

This is the account without bookings page

![Account without booking](static/readme/html-test5.jpg)

This is the thank you page

![Thank you](static/readme/html-test6.jpg)

This is the 404 error page

![404 page](static/readme/html-test7.jpg)

This is the 500 error page

![500 page](static/readme/html-test8.jpg)

## CSS Validator
When running my CSS code through the [CSS Validation service](https://jigsaw.w3.org/css-validator/) I had no bugs.

![CSS Validate](static/readme/css-validate.jpg)

## Python Vaildator
When running my code through the [CI Python Linter Validation](https://pep8ci.herokuapp.com/) I had no bugs or errors. Ive decided to ignore the 2 lines too long errors

This is in my webapp - admin.py

![Python screenshot](static/readme/python-1.jpg)

This is in my webapp - forms.py

![Python screenshot](static/readme/python-2.jpg)

This is in my webapp - urls.py

![Python screenshot](static/readme/python-3.jpg)

This is in my webapp - views.py

![Python screenshot](static/readme/python-4.jpg)

![Python screenshot](static/readme/python-5.jpg)


## JSHint Validator
When running my JavaScript through [JSHint validator](https://jshint.com/) I had no bugs or erros.

* This is for the datepicker

![Javascript screenshot](static/readme/escaperoom-js.jpg)

* This is for the map. I have a couple undefined variable however I used this website to write the code. [Google maps code](https://developers.google.com/maps/documentation/javascript/adding-a-google-map)

![Javascript maps screenshot](static/readme/escaperoom-jsvalidator.jpg)

## Defects

Phone number allows the user to add letters. This is ok as its low level. The email is more reliable and will be used to contact the user first.

## Manual

Testing has been done manually with the google chrome dev tools to make sure the website is fully responsive. I have checked all pages at all key breakpoints to make sure the layout remains user friendly and nothing clashes.

I manually tested all buttons, forms and links to make sure the correct action took place. Here are tables to show the testing.

### Nav bar

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| logo   | Takes you to the home page     | PASS    | 
| Home link     |   Takes you to the home page     | PASS      |
| Rooms link   | Takes you to the rooms page     | PASS    | 
| Book link     |   Takes you to the booking page or sign in/sign up page     | PASS      |
| login/sign up link   | Takes you to the sign in page     | PASS    | 

### Footer

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| google maps   | allows you to see the location     | PASS    | 
| Facebook link     |   Takes you to the facebook page     | PASS      |
| Instagram link   | Takes you to the instagram page     | PASS    | 
| Twitter link     |   Takes you to the twitter page     | PASS      |

### Home page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| hero button   | Takes you to the booking page or sign in/sign up page     | PASS    | 
| popular room link     |   Takes you to the booking page or sign in/sign up page     | PASS      |

### Rooms page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| rooms book button   | Takes you to the booking page or sign in/sign up page     | PASS    |

### Create an account or Sign in to make a booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| sign in button   | Takes you to the  sign in   | PASS    | 
| sign up button     |   Takes you to the sign up page     | PASS      |

### Create an account form page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| sign in link   | redirects to login form   | PASS    | 
| All inputs   | make sure they're all valid   | PASS    | 
| sign up button     |   Creates your account and redirects to home page     | PASS      |

### Sign in form page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Sign up link   | redirects to create an account form   | PASS    | 
| All inputs   | make sure they're all valid   | PASS    | 
| sign in button     |   Sign in to your account and redirects to home page     | PASS      |

### Nav bar dropdown once logged in

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Dropdown   | brings a dropdown for two options   | PASS    | 
| booking link   | redirects to manage booking page   | PASS    | 
| logout link     |   takes you to confirm logout     | PASS      |

### Booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| All inputs   | make sure all inputs are valid before submitting   | PASS    | 
| datepicker   | datepicker should appear   | PASS    |
| timepicker   | timepicker should appear   | PASS    | 
| submit button   | submit form and a confirmation message appears on new page   | PASS    | 

### Manage booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Update button   | takes you to the booking form   | PASS    | 
| Cancel button   | bbrings up an alert to confirm cancel   | PASS    |

### Manage booking bo booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Book button   | takes you to the booking form   | PASS    | 



# Security Features

* Users cannot deduce the delete url and delete others bookings, they get a custom 500 error page if they do this when not logged in and a warning message if they are authenticated

* Users cannot deduce the update ulr and update others’ bookings, they get a custom 500 error page if they attempt to do this.

* Booking Update: Message Failure trying to book a time already booked
* Booking Update: Message failure if not logged in
* Booking Update: Message failure if they dont own booking
* Booking Cancel: Message Failure if not logged in
* Booking Cancel: Message failure if they dont own booking
* Place Booking: User not logged in
* Place Booking: Time & room already booked
* 500 Page: This can be activated for many reasons, but you are able to get there if you try to delete a booking that you don’t own, or if you try to access a booking that doesn’t exist

## User authentication
* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

## Form Validation
* Extensive form validation is used on front end as well as backend.

## Database Security
* All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

# Bugs

## Solved

* I had some contrasting issues which I fixed by using devtools and using their recommended colours

![Contrast](static/readme/readme-contrast1.jpg)

* I had two main bugs in my project. These two bugs would allow hackers to delete and update someone else's bookings. I first had to check if the user that was trying to update or cancel the booking, owned that booking. I done that through this code - 

![Bug](static/readme/escaperoom-bug.jpg)

* Then I had to write an if statement to allow the authenticated user to continue their action. If not they get a custom 500 error page.

![500](static/readme/escaperoom-bug500.jpg)

* I had an issue when refresing on thank you booking page, it sends user another email. I had my email in the wrong section of my code and was a simple fix with a quick move. 

![Email code](static/readme/escaperoom-bugemail.jpg)

* I also had a bug with my messages. If a user were to sign in and sign out, then sign in to another account you would get a long list of messages appear on the my bookings page.

![Message bug](static/readme/escaperoom-bugmessage.jpg)

* To fix this I moved my for message loop out of my_booking.html into the base.html. This meant that the message would appear one at a time instead of a build up of messages once you opened the my_booking.html.

## Left to solve

There are no more bugs to solve as of 18/01/2023


## TECHNOLOGIES USED
- GitPod
- GitHub
- Django
- Bootstrap
- Cloudinary
- Summernote
- Crispy Forms
- Heroku
- Balsamiq
- Fontawesome

## DEPLOYMENT
**Step 1:** Create a new app in Heroku, choose a unique name and region.
**Step 2:** Login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region).
**Step 3:** Return to dashboard, copy the database URL:
<img width="800" alt="image" src="https://user-images.githubusercontent.com/97494262/209531384-85d95cc3-a381-4c3c-b56f-215238e0daf8.png">

**Step 4:** Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:

<img width="372" alt="image" src="https://user-images.githubusercontent.com/97494262/209531222-599282ee-2c54-490f-b543-1f09e5255490.png">

**Step 5:** Include a secret key in the variables:

<img width="800" alt="Screenshot 2022-12-26 at 11 25 13" src="https://user-images.githubusercontent.com/97494262/209531979-9ba177cc-3e44-48a7-80dc-884d06932f54.png">

**Step 6:** Include the below code to settings.py file:

<img width="301" alt="image" src="https://user-images.githubusercontent.com/97494262/209532128-acaa1e29-edea-45c3-93ce-2caaf0f71862.png">

**Step 7:** Link the database in settings.py and migrate then push to GitHub:

<img width="303" alt="image" src="https://user-images.githubusercontent.com/97494262/209532393-5283592f-5caf-4e81-b3fd-9d20bd62b111.png">

**Step 8:** In Heroku, add three config vars:

<img width="243" alt="image" src="https://user-images.githubusercontent.com/97494262/209532605-04bff00b-951f-4084-9ad5-6eff111ac6bf.png">

<img width="350" alt="image" src="https://user-images.githubusercontent.com/97494262/209532533-e9b3d879-a40a-4335-a56b-3c0e5c370a8a.png">

**Step 9:** Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:

<img width="571" alt="image" src="https://user-images.githubusercontent.com/97494262/209533286-4a79143c-6568-4055-99fc-76dd5821a02b.png">

**Step 10:** Add cloudinary to installed apps in settings.py, add static/media file settings:

<img width="407" alt="image" src="https://user-images.githubusercontent.com/97494262/209533445-8f6670c5-490b-4294-95cf-febaaaed2ab2.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/209533629-ab3fb31b-f096-4305-996e-970e4c950a3f.png">

**Step 11:** Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/97494262/209533879-b8284837-e7a1-4315-83e6-9b88d2125882.png">

<img width="501" alt="image" src="https://user-images.githubusercontent.com/97494262/209534100-46723f98-7bd6-40ed-91c1-5226ad6e950d.png">

<img width="313" alt="image" src="https://user-images.githubusercontent.com/97494262/209534271-772afed4-f299-45dc-b72d-d0843b7ad189.png">

**Step 12:** Create a Procfile, then commit and push to GitHub:

<img width="504" alt="image" src="https://user-images.githubusercontent.com/97494262/209534389-5b0cdd3c-54f7-44e8-8a21-99068431365a.png">

**Step 13:** Connect GitHub account in Heroku, connect and deploy branch. Open app and check:

<img width="421" alt="image" src="https://user-images.githubusercontent.com/97494262/209534580-c03fa4fd-8e52-487b-8ecc-23563fd30327.png">

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The articles on the blog were written myself and any additional helpful articles were linked to for the user to access for more information.

### Media
- The fonts were chosen with guidance from an article written by Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The colors for the website was generated using [Color Space]([https://coolors.co/image-picker](https://mycolor.space/?hex=%2333C883&sub=1)).
- The plant images were sourced using [Pexels](https://www.pexels.com) and [Pixabay](https://pixabay.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
