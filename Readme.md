# Manguezal Brewery – Manguezal Club
## Data Centric Development Milestone Project 

### User eXperience

    This web application was made for users who would like to make a review about the Manguezal Brewery beers and also have access to other user’s reviews. At the moment the company has 3 types of beers but eventually a different types are made for special occasions giving the option for user to add new beers and make a review about them as well. 
    The market that I want to achieve is over age people who appreciate a good beer, and add value to the company. People who enjoy making part of a group where they can share experience with other people. Also those users will be able to read others reviews and make them able to edit and delete their own review. On the webpage users will be able to have more information about the company such as social media and information about the brewery process.
    As a user I want to be able to:
	1. make a comment a review about the beers I have tasted;
	2. edit the review made (review, date, name or beer);
	3. delete my review.

### Demo

A live demo can be found [here](https://manguezalclub.herokuapp.com/)

A print screen is shown belo with the home page on Mobile and Ipad:
<table>
  <tr>
    <td>Home on Mobile</td>
     <td>Home on Ipad</td>
  </tr>
  <tr>
    <td><img src="https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/mobile.PNG?raw=true" width=270 height=480></td>
    <td><img src="https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/ipad.PNG?raw=true" width=350 height=480></td>
  </tr>
 </table>

#### Scrreshots
 Please check the link to see a screenshot of each section.
[Home]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/home1.PNG?raw=true)

[About]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/home2.PNG?raw=true)

[Contact]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/home3.PNG?raw=true)

[Add a review]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/review.PNG?raw=true)

[Add a beer 1]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/addbeer1.PNG?raw=true)

[Add a beer 2]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/addbeer2.PNG?raw=true)

[Manguezal Club 1]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/manguezalclub1.PNG?raw=true)

[Manguezal Club 2]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/screenshots/manguezalclub2.PNG?raw=true)


#### Wireframes:

[Home]( https://github.com/Pauloa90/Flask-final/blob/master/static/images/wireframes/screen1.jpeg?raw=true)

[Add a beer](https://github.com/Pauloa90/Flask-final/blob/master/static/images/wireframes/screen2.jpeg?raw=true)

[Manguezal Club](https://github.com/Pauloa90/Flask-final/blob/master/static/images/wireframes/screen3.jpeg?raw=true)

### Skeleton
	**Strong text** Home Page
On this section the user will get to know more about the company and purpose of the website. As they scroll the page down they will see a section with the ingredients, one section about the company and also a form to get in contact with the company staffs.
	**Strong text** Review
This section the user is able to add a review about one of the 3 beers that the company produces and if the user tried a special limited edition not listed on the website, on this section they will be also able to add a type of beer and a comment afterwards.
	**Strong text** Manguezal Club
On this section user will able to read others people review and also edit their own review in case they did a mistake by accident.
	**Strong text** Add a different beer
On this section a simple form is displayed where users will be able to add a different type of beer.
	**Strong text** Edit a review
On these section users will be able to edit a review in case they did a mistake typing the review or choosing the beer. Also if the users don’t want their review on the website they will be able to delete it as well.

### Feature
	#### Existing
1. Create review form – this will allow users to either create a new review. The review will be inserted into the database in case of adding.
* Read – by clicking on “manguezal club” the user will be able to read all the reviews made so far.
* Edit review (update) – this will allow the user to edit a review, updating it in the database.
* Delete a review – this will allow the user to delete one of the reviews removing from the database.
* Edit a beer type – this will allow the user to add a different type of beer that the users might have tried but is not listed.

	#### To be implemented
* Login – This feature would allow users to only delete and edit their own review. Also the company gets leads to work on promoting the company.
* Like dislike/Most popular – This feature would allow users to check the best rated beers and most popular among customers.
* Email API - This feature would allow the company to get users contact details.
* Subscribe – This feature would allow the company to send automatically news about the company.

### Technologies Used
**Strong text** HTML
This project uses HTML5 to build the foundation of the application. Templates were used as well in order to not repeat the code written.
**Strong text** CSS
This project uses CSS in order to style the components on HTML.
**Strong text** Bootstrap
The most popular frontend framework was used to make the application responsive and well designed.
**Strong text** Python
The application is built on python language.
**Strong text** Flask
In order to make the frontend and backend of the application connected, Flask a micro framework, was used. A “base” template was made in HTML and using Flask I connected the “base” to repeat on others webpages the code specified.
**Strong text** MongoDB
All the data storage is using MongoDB. 2 collections were created to store the date sent by the users.
Font Awesome
In order to make the design and the user experience better I used Icons taken from Font Awesome.
**Strong text** Google fonts
This project users Google Fonts to provide fonts for the headings of the web application.

### Testing

This web application has been tested on different browsers using computer and smartphones that the user may experience.
####	Home Page 
The Navbar will be fixed on the top of the screen all the time. That will make the user not lose the track when they want to go to a different page. On the button “Share experience” on the first image, on click the user will be redirect for the “add review” section.
As the user scroll the page down, two images will appear with the parallax effect giving a nice user experience.
The user will get to know more about the brewery and a contact form will appear where the user can get in contact with the company for any future event or any question that they may have.
On the footer we have more information about the company such as the email address and te telephone number. The links to brewery’s social media. If they user clicks on them, another page tab will load the links in order to keep the user on the loop. In order to that I used “_black” as target on those links. At the moment the company uses only Instagram and a Facebook page. In the future they will create a YouTube channel to promote and brand such as a Twitter to promote their events and news. For now, those two links are redirecting to the social web page medias.
A subscribe button on the footer is given as an option for the company in case in future they want to create newsletter for users who subscribed on the webpage.

####	Others sections
On the navbar if the user clicks on review, a form will load on the a new page with the inputs name, date, beer, review and a button to add the review and inset the data into the database. After clicking on “Add a review” the user will be redirected to “manguezal club” page.
On the section Manguezal Club the user can read all the reviews added so far on the application. The reviews are being retrieved from Mongo DB. For now, as no login system was implemented, users can edit and delete any reviews. When the login is implemented the user will be able to change just their own data.

### Responsiveness Testing

This application has been tested on all mobiles, tablets and desktop screen sizes in order to check if it is responsive.

### Deployment

The source of this code can be found on Github and the app has been deployed into Heroku as Heroku can run python applications.
In order to install the application, the steps were followed as mentioned below:
Download the repository
Login on Heroku
Click on “Create a new App”
Enter a unique name for the application
From the command line on GitPod follow the commands:
    1.Pip3 install Flask
    2.Pip3 install pymongo
    2.Pip3 install dnspython
    3.Pip3 freeze –local > requiremets.txt
    4.Echoweb: python run.py > Procfile
    5.Git add .
    6.Git commit –m “initial commit”
    7.Git push –u heroku master
    8.Heroku ps: scale web=1
*From Heroku set IP: 0.0.0.0, PORT :5000, MONGO_URI: mongodb://[username]:[password]@ds129914.mlab.com:29914/reviewmanguezalclub
*On “More” from Heroku click on Restart all Dynos

### Credits and Acknowledgements 

* The first picture on Home Page can be found on [Unsplash]( https://unsplash.com/photos/46Yad80Ynp4)
* The text on the section “About” and the others  pictures of manguezal beers can be found [here]( https://cinemaecerveja.com.br/cervejaria-manguezal-e-sua-inspira%C3%A7%C3%A3o-no-ecossistema-do-recife-f6d8b8a41213)
* Ingredients:
1. The grain picture and the hops can be found [here]( https://beerandbrewing.com/VMksOysAAKGj4ZKw/article/noble-hops-cheat-sheet/)
2. The yeast picture can be found [here]( https://learn.kegerator.com/dry-yeast/)
