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


- [X] C - Site users can create/register their own profile to interact with the plant posts.
- [X] R - Site users can open and read the plant blog posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a plant detail post.
- [X] D - Site users can eliminate their like if desired on a plant detail post.


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


- [X] C - Site users can create their own comments using a form on each blog post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

* ### Comment
This data model is used to store the comments of the users along with their sentiments:

| Field       | Data Type         | Purpose                                  | Form Validation                  |
|-------------|-------------------|------------------------------------------|----------------------------------|
| pk          | unique Identifier |                                          |                                  |
| stock       | ForeignKey        | One to many relation w/StockInfo         | required but automatic           |
| name        | CharField         | To be shown below comment                | required but automatic           |
| email       | EmailField        | To be stored in database                 | required but automatic           |
| body        | TextField         | To be shown, it is the comment           | required                         |
| created_on  | DateTimeField     | To be shown below the comment            | required but automatic           |
| approved    | BooleanField      | To let admin approve before publishing   | required, auto is False (*)      |
| sentiment   | CharField         | To express the sentiment                 | required, default is HOLD        |

(*) Please notice that in the current version and for better interactivity for the users, not yet approved comments are also shown on the site.

## TESTING

### Validation Testing
- HTML
   - No errors were returned when passing through the official [HTML validator]("https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F").

**Post List**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156718-b0e52c29-0edf-46b7-9e13-eed62b1bb787.png">
   
**Post Detail**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156567-eb2b02a0-596a-4a52-ade9-213ee00dfbae.png">

**Sign up**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156724-f2aab13c-453a-4556-9a5a-af64cff6f888.png">

**Sign in**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156731-bf8dfff2-c326-4ebb-a826-905e213f9536.png">

**Edit Comment**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156740-9699a4c3-1671-489f-b869-760ba3de554f.png">

- CSS
   - No errors were found when passing through the [CSS validator]("https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en").

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210075568-6efc11bf-8f09-4ec8-8eae-c3936a1678df.png">

- JavaScript
   - No errors were found when passing through the [JS validator]("https://jshint.com/").
   
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210155726-28197ad7-5f34-49d1-bc1c-5991f2b29533.png">

### Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers.

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** |
|-----------------------------|------------------|---------|------------------|
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |
| dev tools: Pixel 2          | Chrome           | android | 411 x 731        |
| real phone: iPhone XR       | safari           | iOs     | 414 x 896 px     |
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |
| browserstack: iPhone 13 Pro | safari           | iOs     | 390px × 844px    |
| real tablet: iPad Pro 11    | Chrome           | iOs     | 834 x 1075 px    |
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |
| browserstack                | Edge 99          | windows | 1440 x 672 px    |

### Manual Testing
- You can view manual testing of the website [here](https://docs.google.com/spreadsheets/d/123Pia98Ms_Fe6at0hPnAWhcNrmeVc4X2RLYmD7VsqX4/edit?usp=sharing).

### Automatic Testing
- Manual testing was done due to time constraints.

### Outstanding Defects
- There are no outstanding defects.

### Defects of Note
- The user story for [OPEN A POST](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/issues/8) had multiple challenges including styling issues with the summary card, the likes/comments area and rendering of the plant detail model information. 
 - The styling challenges were solved using margins and restructuring of some div elements.
 - The comments/likes area required some guidance from my mentor to establish what the user sees when logged in, logged out and restructured the template from there.

## ACCESSIBILITY

### Lighthouse Audit
- The deployed website was run through lighthouse to check performance, accessibility, best practices and SEO scores.

<img width="650" alt="image" src="https://user-images.githubusercontent.com/97494262/210155754-2d11ca71-a553-47a9-a94b-41fd4c1aebd9.png">

### Keyboard Navigation
- The users will be able to use the tab button to navigate the website if required.

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
