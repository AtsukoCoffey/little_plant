# LITTLE PLANT shop

LITTLE PLANT shop is an online indoor plant's shop. Forcusing the type of plants like Succulents, Air plants and some other easy-care plants for busy people.
It's fully functioning e-commerce web application, that allows users to view and purchase, register account, record past orders, also able to post reviews and send messages from contact form.

## UX DESIGN

### 1. Strategy Plane

#### Target users
1. Busy people who like easily managed plants.
2. People who are looking for green decor as interior design.
3. People who are new to growing plants.
4. Everyone who loves living plants.

#### User value
1. Users can find the benefits - Air purification, Natural beauty, Reduction in positive ions
2. Users can choose their matched plant items to thier life styles.

### 2. Scope Plane
* As a First-Time Visitor
  * I want to clearly understand what services are offered on this website.
  * I want to be able to easily navigate through to find contents.
  * I want the website to work on different devices and formats that I use.
  * I want to view all available products to compare and choose.
  * I want to see the product's detailed information.
  * I want to easily view the total of my purchases at any time and find the total cost clearly. 
  * I want the payment process to be secure, simple and easy.
  * I want the notification on screen from my action to ensure that my action is valid.
  * I want the email confirmation on my order.
  * I want to see other customers' reviews and rating scores related to the products.
  * I want to see the site owner's real address and SNS channels to feel confident.
  * I want to send my query easily through the contact form. 
  * I want to register my email for Newsletter to receive information about sales and new plant product arrivals.
  * I want the input search bar to be in a convenient position.
  * I want the FAQ page to learn more support information such as "returning" and "shipping".
* As a Returning and Frequent Visitor
  * I want to register an account to store my personal information for easier shopping next time.
  * I want to view my past order records to ensure my new order is sent to the system properly.
  * I want to share and manage my rating score and reviews.
  * I want to reset my password in case I forget it.
* As a Website owner 
  * I want to clearly convey who we are and give users a sense of trust and confidence.
  * I want to login as an administrator to have a permission to manage the site. 
  * I want to manage the plant products. ( Create, Read, Update, Delete )
  * I want to view and and manage all customer orders.
  * I want to view, reply to, and manage the customer queries from the contact form.


### 3. Structure Plane

### 4. Skeleton Plane
#### Information Archtecture
First-time visitor ( Not logged-in )  
![Information Archtecture](documentation/ia-first-time-visitor.png "Information Archtecture")  
Frequent visitor ( Logged-in )  
![Information Archtecture](documentation/ia-frequent-user.png "Information Archtecture")  
Administrator  
![Information Archtecture](documentation/ia-administrator.png "Information Archtecture")  

#### Database relationship diagram
![Database relationship diagram](documentation/db-diagram.png "Database relationship diagram")  

#### Wireframes
Top-page 1440px width monitor  
![Wireframes Top-page 1440px width](documentation/wireframe-top1440.png "Wireframes Top-page 1440px width")  
Top-page Navigation Dropdown  
![Wireframes Top-page 1440px width](documentation/wireframe-top1440-nav-drop.png "Wireframes Top-page 1440px width")  

Plant Product list page    
![Wireframes Plant Product list page 1440px width](documentation/wireframe-product-list1440.png "Wireframes Plant Product list page 1440px width")  
Plant Produnct detail page  
![Wireframes Plant Produnct detail page 1440px width](documentation/wireframe-product-detail1440.png "Wireframes Plant Produnct detail page 1440px width")  

Shopping Bag page    
![Wireframes Shopping Bag 1440px width](documentation/wireframe-bag1440.png "Wireframes Shopping Bag 1440px width")  
Checkout page  
![Wireframes Checkout page 1440px width](documentation/wireframe-checkout1440.png "Wireframes Checkout page 1440px width")  

About-us & Contact-us page  
![Wireframes About-us 1440px width](documentation/wireframe-aboutus1440.png "Wireframes About-us 1440px width")  

Plant Produnct Add page   
![Wireframes Plant Produnct Add page 1440px width](documentation/wireframe-product-add1440.png "Wireframes Plant Produnct Add page 1440px width")  
Plant Produnct Edit page   
![Wireframes Plant Produnct Edit page 1440px width](documentation/wireframe-product-edit1440.png "Wireframes Plant Produnct Edit page 1440px width")  

## FEATURES
### Existing Features 
#### Site Pages

* Homepage  
  * Navigation bar
  * Login Dependant Account links
  * Product's search bar
  * Some recomended contents in the Bootstrap's carousel
  * Newsletter Registeration
  * Display account authentication status
  * Logged-in user's only  
    * Access link to profile page
    * Prefill user's registerd email address in the News Letter form
  * Admin's Features  
    * Add a new plant product
    * Link to Order manage page
    * Link to Contact query manage page
* Authetication pages
  * User Registration
  * User Login
  * User Logout
* Profile page
* Product list view page
  * Ordered by name, price and search 
* Product detail's page
  * Add in the shopping bag
  * reviews and star rating scores
  * Admin's Features
    * Buttons to edit and delete the product
* Shopping bag
  * Button to Checkout
* Checkout
  * Users can payfor products using credit/debit card.
  * Users receive comfirmation emails 
* About us page
  * Contact form
* Review page
* 
* Other pages
 * User Features  
   * Authentication Password reset
   * Toasts - 

### Future Features



## WEB MARKETING
### Ecommerce Businness Model
This shopping site sells plant's product to individual customers ( end-users ) with single Payment so the businness model is B2C ( Bussiness to Customers ).

Newsletter registration, Facebook and other SNS links

## User story
| Epic | User Story ID | AS A/AN | I WANT TO BE ABLE TO ... | SO THAT I CAN ... |
|-|-|-|-|-|
| Environment Configuration	| Create project structure | Developer | Create the project structure | Start develop this project |
|-| Install crispy and other modules | Developer | Set up other useful modules | Use forms and images easily |
|-| Connect CI database | Developer | Set up Database - SQLite3 and PosgreSQL | Prepare to use both in case testings or problems |
| Home app | Create homepage app and index template | Developer | Create homepage app and template | Runserver to check the page in browser preview|
|-| Create Navigation bar and footer | Site User | Find the site content's links instinctively | Easily navigate through to find contents |
|-| Sort the product list by categories and sale | Site User | Quickly identify categories and special offers | Take advantage of special savings on products I'd like to purchase |
|-| The current login status is reflected to status mention area | Site User | See my logging-in account name | Aware of my account logging in status |
|-| Newsletter's form - footer | Site User | Find Newsletter form | Apply it from all the pages |
| User Authentication | User Registration |	New Site User | Register an account | Store my personal information for easier shopping next time |
|-| User Log in / Log out | Site User | Easily login or logout | Access my personal account information |
|-| Reset Password | Site User | Easily recover my password in case I forget it | Recover access to  my account |
|-| Email confirm - Registration | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Product app | Product List view | Site User | View all available products | Find out some products that I can compare and choose |
|-| Product detail view | Site User | View the specific product's information | Inspect the details before purchasing it |
|-| Product create | Administrator | Create the new product | it will be added to the list page |
|-| Product edit | Administrator | Edit the product | To manage the products |
|-| Product delete | Administrator | Delete the product | To manage the products |
| Profile app | Store and edit personal information | Site User | Store personal information | Prefill those for my future orders |
|-| Store my past order records | Site User | Store my past order records | Ensure my new order is sent to the system properly |
| User Experiense | Clear visual information and title | Site User | clearly understand what services are offered on this website | View the site with a purpose |
|-| Attractive Carousel | Site Owner | Show some nice contents to attract site users | Guide Site users to visit those pages |
|-| Toasts notification | Site User | Rceive the notification on screen from my action | Ensure that my action is valid |
|-| Breadcrumb | Site User | Know where I am now and how to go back to other pages | Freely move around to the desired pages |
|-| Pagination for the query data | Site User | Use page navigation for query data | View next page of the same query |
|Product Reviews| Create Reviews, Special-offer and other templates | Developer | Provide templates and views for reviews and special offers | Pages can be created from product filtering |
| About us app | Create About us app, template | Site Owner | clearly convey who we are	| Give users a sense of trust and confidence |
|-| About us - Contact form	| Site User | Use the simple easy form | Send my query easily through the contact form |
|-| Admin - Query list | Administrator | View all queries and select box for change status | manage multiple customer queries |
|-| Admin - Query detail | Administrator | View indivisual query and reply the message by email	| Change status or delete the query |
| Sorthing | Category sorting | Site User | Sort the specific category of product | Find the best product in a specific category |
|-| Product search bar | Site User | Search for a product by name or description | Find a specific product that I'm looking for |
|-| Search result | Site User | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |