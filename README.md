# Album Review

## Author
Dylan Groome

## Project Overview
*  The Album Review is a place for discussion about the most influential rap albums. Each album post is dedicated to a popular artist , with a detailed description. 
* You can view the deployed website [here]https://pro-4-album-ranking.herokuapp.com/).

<img width="1439" alt="Screenshot 2023-04-30 at 07 34 18" src="https://user-images.githubusercontent.com/108524172/235340480-0bb17896-907f-4670-bcbd-64f7794ea745.png">


## TABLE OF CONTENTS
- [Album Review]
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

### Home
- The home page was designed using cards to show a quick summary of each albume.
- The user can click and find out more about a album that interests them.
![home](https://user-images.githubusercontent.com/108524172/235346650-a8d20d67-7777-4871-91cb-3537402a8f04.png)


### Album Detail
- Each album post provides detail about the album. 
- The registered user can also comment and like the post if desired.
![album](https://user-images.githubusercontent.com/108524172/235346676-1e8987d7-e4d9-428a-a061-ef2785e409e2.png)

### Artist Detail
- Each artist post provides detail about the artist. 

![artist](https://user-images.githubusercontent.com/108524172/235346710-d531284d-af2c-4fcf-9886-643f603081de.png)


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
![Artist] <img width="588" alt="Screenshot 2023-04-30 at 09 41 31" src="https://user-images.githubusercontent.com/108524172/235344041-4d7245db-e678-4851-b246-b490f20d39be.png">


### Account Page

![Account]<img width="612" alt="Screenshot 2023-04-30 at 09 43 06" src="https://user-images.githubusercontent.com/108524172/235344072-f5a4e9c4-8a1d-42db-bd6a-74fbf3b5cea7.png">

* ### HTML Validator 
All HTML pages' code successfully passed through HTML Validator with no errors.
![HTML Validator]<img width="1052" alt="Screenshot 2023-04-30 at 10 00 44" src="https://user-images.githubusercontent.com/108524172/235344793-764e4313-18d1-4286-b2e3-5b08c687c0d4.png">


## CSS Validator
When running my CSS code through the [CSS Validation service](https://jigsaw.w3.org/css-validator/) I had no bugs.

![CSS Validate]<img width="1030" alt="Screenshot 2023-04-30 at 10 07 51" src="https://user-images.githubusercontent.com/108524172/235345107-b3a0f776-130b-408f-8be1-5b11e4b50bab.png">


## Python Vaildator
When running my code through the [CI Python Linter Validation](https://pep8ci.herokuapp.com/) I had no bugs or errors.


<img width="1364" alt="Screenshot 2023-04-30 at 10 13 22" src="https://user-images.githubusercontent.com/108524172/235345326-5da73713-60b7-4325-9995-14f85123a1d8.png">


## JSHint Validator
When running my JavaScript through [JSHint validator](https://jshint.com/) I had no bugs or erros.


![Javascript screenshot]

<img width="1047" alt="Screenshot 2023-04-30 at 10 17 38" src="https://user-images.githubusercontent.com/108524172/235345477-3b0459d2-cb4e-4634-bfca-49182c91a671.png">


## Defects

No defects

## Manual

Testing has been done manually with the google chrome dev tools to make sure the website is fully responsive. I have checked all pages at all key breakpoints to make sure the layout remains user friendly and nothing clashes.

I manually tested all buttons, forms and links to make sure the correct action took place. Here are tables to show the testing.

### Nav bar

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| logo   | Takes you to the home page     | PASS    | 
| Home link     |   Takes you to the home page     | PASS      |
| login/sign up link   | Takes you to the sign in page     | PASS    | 


### Home page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| album title   | Takes you to the album page     | PASS    | 
| album image     |   Takes you to the album page   | PASS      |

### Artist page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| artist detail paage   | Takes you to the artist detail page      | PASS    |

### Create an account or Sign in 

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


### comment/rate page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| All inputs   | make sure all inputs are valid before submitting   | PASS    | 
| submit button   | submit form and a confirmation message appears on new page   | PASS    | 

### edit comment page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| edit button   | takes you to the edit form   | PASS    | 


### delete comment page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| delete    | deletes comments   | PASS    | 



# Security Features

* Users cannot deduce the delete url and delete others comments


## User authentication
* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

## Form Validation
* Extensive form validation is used on front end as well as backend.

## Database Security
* All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

# Bugs

No bugs


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


**Step 4:** Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:



**Step 5:** Include a secret key in the variables:



**Step 6:** Link the database in settings.py and migrate then push to GitHub:


**Step 7:** In Heroku, add three config vars:


**Step 8:** Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py:


**Step 9:** Add cloudinary to installed apps in settings.py, add static/media file settings:


**Step 10:** Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:


**Step 11:** Create a Procfile, then commit and push to GitHub:


**Step 12:** Connect GitHub account in Heroku, connect and deploy branch. Open app and check:


## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The articles on the blog were NOT written BY myself  helpful articles were linked to for the user to access for more information.
- https://www.youtube.com/watch?v=FawGmAas4h0&list=PL9tgJISrBWc6ktmvTSLGrn055XzVb0OwZ
- https://www.rollingstone.com/music/music-album-reviews/nothing-was-the-same-125752/
- https://www.udiscovermusic.com/artist/drake/
- https://www.biography.com/musicians/j-cole
- https://www.britannica.com/facts/Kanye-West
- https://www.udiscovermusic.com/artist/kendrick-lamar/


## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
