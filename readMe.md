# Top 10 Movies - Data Centric Milestone Project #

### Project Info ### 
My goal is to make a "Top 10 List.." website. A website where anybody can view Top 10 lists that other users have made, or create and edit Lists of there own. At the beginning my plan was to make a site without any set category, and where you could create a list of whatever topic you may choose. I realised that that was a little bit to much in such a short time, combined with limited skills in the area (so far), so I narrowed it down to the topic; Movies.

### UX ###

The main UX goal with the website, is to provide a sence of fun and warmth. Colorful, but soft features, and a "round" font style will hopefullt accomplish this.
  
#### User Stories: ####

1.	As a visitor looking for inspiration for my movie-night, I'm looking for the best movies in a specific category.  

2.	As a visitor who wants to share my movie experience with other people, I want to create a list of my recommendations in an easy way.

3.	As a visitor looking for a what other peoples opinions are concerning movies, I want to browse their lists of favourite movies.                 

#### Strategy ####

I wanted to make a website that would make the visitor want to stay and explore further, because it's both easy and what the user is looking for.

#### Scope ####

A simple and self-explanatory layout and homepage, with warm colors and an "easy-on-the-eye" look.

#### Structure ####

Firstly, I decided on the structure for the navigation and architecture of the website. I wanted it to be self-explanatory and easy to "move around". Next I planned for the list-display, and how I wanted visitors to reach the lists. I decided that the best way was to use a sidebar where all the lists was displayed and when clicking on any list, you would get to the content of that specific list. Next, I realised that I wanted the visitor to be able to create an account, in order to be able to create their own list and put their label on them. For this, I needed a "Sign In" page, and a "Sign Up" page. The user was then going to be able to both create a list (through a form on a sepperate "Create List" page, and edit their existing lists as well). 

#### Skeleton ####

![Wireframe](./wireframes/create-list-wireframe.png)
![Wireframe](./wireframes/home-page-wireframe.png)
![Wireframe](./wireframes/sign-in-wireframe.png)
![Wireframe](./wireframes/view-lists-wireframe.png)

#### Surface ####

I wanted the surface to represent calmness and fun. I tried a few different color shades aswell as images of different sort, but in the end I decided to go with the 2 main shades both in the turqouise area, but 1 more to the blue side and 1 more to the green side. To make the page to be a little more "alive" I added a yellow color on a few details. 

### Features ###

#### Existing Features ####

-   Register: lets a visitor register with a unique username and password. 
-	Log In: lets a user log in.
-	Log Out: lets an already logged in user log out.
-	View List: lets a visitor browse through excisting lists. 
-	Create List: lets a user create a list.
-	Edit/Delete List: lets a user edit or deleta a list of their own creation.



#### Features Left to Implement ####

In the future:
- I would like to make it possible for a user to add images for each list-object when they create a list.
- I would like to make it possible for users to comment and rate other users list. 

### Technologies Used ###

-   Python (Flask)
-   MongoDb (as Database)
-	HTML
-	CSS
-	Bootstrap 4.1.0: https://getbootstrap.com/
-	Pixabay: https://pixabay.com/ (for all images)

### Testing ###


##### Testing Responsiveness #####
The code and website have been tested through-out a number of different Browsers (Chrome, Firefox, Explorer) and on a number of different devices via Google Chromes Developer Tools, to check responsiveness (different mobile devices like Iphone & Samsung Galaxy, Ipad, etc.) 

##### Testing User Stories #####
Since all of my User Stories are, in the end, a matter of taste, I have a difficulty of proving that they where fully accomplished. Of the 3 different persons who "played around" on the website (created a user and created a list), they all found it fun and had a good time making lists. 

### Errors/Problems ### 

1 (big) error has not yet been fixed due to time-schedule. When a user creates a list, and then goes to update/edit that list, the content of all the list-objects dissapears and you have to put it in all over again. A pretty big problem if you want to just edit 1 small thing in a list.     

### Deployment ###

The website is deployed on Heroku. To check out the live website, follow this link: https://top-ten-movies.herokuapp.com/home
Github: https://github.com/AntonIsaksson/milestone-project-3 


### Content ###

All written content is made by myself.

### Media ###

All pictures is taken from https://pixabay.com/