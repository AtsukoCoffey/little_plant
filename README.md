# LITTLE PLANT shop

LITTLE PLANT shop is an online indoor plant's shop. Forcusing the type of plants like Succulents, Air plants and some other easy-care plants for busy people.
It's fully functioning e-commerce web application, that allows users to view and purchase, register account, record past orders, also able to post reviews and send messages from contact form.

## Live site [LITTLE PLANT shop](https://little-plant-shop-e08318b823f1.herokuapp.com/)


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
These are my original plan's User sories.
In develop phase user stories are here [User story Testing in TESTING.py](https://github.com/AtsukoCoffey/little_plant/blob/main/TESTING.md#user-story-testing) 


### 3. Structure Plane

### 4. Skeleton Plane
#### Information Archtecture
First-time visitor ( Not logged-in )  
![Information Archtecture](documentation/ia-first-time-visitor.png "Information Archtecture")  
Frequent visitor ( Logged-in )  
![Information Archtecture](documentation/ia-frequent-user.png "Information Archtecture")  
Administrator  
![Information Archtecture](documentation/ia-administrator.gif "Information Archtecture")  

#### Database relationship diagram
<details>
<summary>Diagrams in the initial planning phase</summary>

![Database relationship diagram](documentation/db-diagram.webp "Database relationship diagram")  
</details>
There were several changes, and the final result was this.   

![Database relationship diagram](documentation/db-diagram2.webp "Database relationship diagram") 

#### Wireframes
Top-page 1440px width monitor  
![Wireframes Top-page 1440px width](documentation/wireframe-top1440.png "Wireframes Top-page 1440px width")  

<details>
<summary>Top-page Navigation Dropdown  </summary>

![Top-page Navigation Dropdown  ](documentation/wireframe-top1440-nav-drop.png "Top-page Navigation Dropdown  ") 
</details>

<details>
<summary>Plant Product list page</summary>

![Wireframes Plant Product list page 1440px width](documentation/wireframe-product-list1440.png "Wireframes Plant Product list page 1440px width")  
</details>
<details>
<summary>Plant Produnct detail page </summary>

![Wireframes Plant Produnct detail page 1440px width](documentation/wireframe-product-detail1440.png "Wireframes Plant Produnct detail page 1440px width") 
</details>

<details>
<summary>Shopping Bag page</summary>

![Wireframes Shopping Bag 1440px width](documentation/wireframe-bag1440.png "Wireframes Shopping Bag 1440px width") 
</details>

<details>
<summary>Checkout page</summary>

![Wireframes Checkout page 1440px width](documentation/wireframe-checkout1440.png "Wireframes Checkout page 1440px width")
</details>

<details>
<summary>About-us & Contact-us page </summary>

![Wireframes About-us 1440px width](documentation/wireframe-aboutus1440.png "Wireframes About-us 1440px width") 
</details>

<details>
<summary>Plant Produnct Add page </summary>

![Wireframes Plant Produnct Add page 1440px width](documentation/wireframe-product-add1440.png "Wireframes Plant Produnct Add page 1440px width")  
</details>

<details>
<summary>Plant Produnct Edit page/summary></summary>

![Wireframes Plant Produnct Edit page 1440px width](documentation/wireframe-product-edit1440.png "Wireframes Plant Produnct Edit page 1440px width")     
</details>  

### Surface

#### Fonts
   
* Logo font - Handlee  
Since our target users are office workers and busy people, I was looking for a font that was friendly and legible, with an image that was not too heavy. That's why I chose Handlee.  

* Body font - Comfortaa  
The main font is the same strategy as the logo font, but it needs to be more readable and less individualistic to be read a lot. We don't want to choose a font that fights with my logo font. This Comfortaa is suitable for the body font I think.

#### Colour scheme 　
Since we sell natural greens, I felt that colors that evoke nature were inevitable. Also chose to avoid strong colors as much as possible to create an airy atmosphere.


![Colour scheme](documentation/colour-scheme.png "Colour scheme")  

## FEATURES  

### Existing Features 
#### Site Pages

1. Homepage 
 ![screen shot](documentation/brows-chrome.png)  
 Top page design:  
 I set the hero image height is 92%, the reason is I wanted to imply there still is some contents under neath, to scroll down to see more contents.  

  * Navigation bar  
  ![screen shot](documentation/feat-nav-bar.png)

    * Display account authentication status and Login Dependant Account links  
    Depending on the user account, navigation contents will be changed. One thing that is easy to spot is the display of user names on the Navbar. Also authentication option will be different and only administrator has `Product Management` access. Logged-in user\'s only have access link to profile page.

    * Shopping bag and Total cost  
    Bag icon leads us to the bag page. This bag is using session so we can access from any pages so that we can put product into the bag anytime and let us know the total cost everytime put in.  

    * Product\'s search bar  
    Search the products that matches the keyword in it's name and description fiealds. If no input to submit Bootstrap toast will let us know.   
    ![screen shot](documentation/feat-error-search-criteria.png)  

    * SHOP PLANTS links  
    All Products shows all the products and other options are filterd by each categories. SPECIAL OFFER is also one of the product list though the filter is not category, If the product has sale price and the value is not 0 nor Null, listed here.

    * FAQ page links  
    FAQ also has the categories that from products information to delivery or privacy policy Q&A   
    
    * Reviews page  
    Authenticated users can write the review from product details pages. This Review page is those reviews collection. The purpose is to see what kind of product is popular or has complains. Also expect the users can share their plants pictures with us  

  * Main Hero image  
    The image I picked was in the free image's website (Unsplash)
    Beautiful colours of succulents were so attractive.  

    * Some recomended contents in the Bootstrap\'s carousel  
    Underneath the Hero image I placed Bootstraps Carousel. This is also draw people's eyes as a kind of animation feature.  
    ![screen shot](documentation/feat-carousel.png)

  * Footer
    The footer appears on all pages so be seen frequently. Important information and Newsletter's link are here from a marketing standpoint.
    * Newsletter Registeration
    ![screen shot](documentation/feat-footer.png)
    
2. Authentication pages  
  * User Registration   
  ![screen shot](documentation/feat-signup.png)
  * User Login   
  ![screen shot](documentation/feat-login.png)
  * User Logout
  ![screen shot](documentation/feat-logout.png)  

3. Profile page   
![screen shot](documentation/feat-profile.png)   
I am using the Profile page and Shopping bag, Checkout sysytem those were taken over from LMS learning walkthrough.
 
4. Product list view page  
![screen shot](documentation/feat-product-list.png)   
  * Products can be filtered by categories, I set useful category filter button on top left corner. Right top corner is sorting dropdown option. Sorting by name, price, categories and by rating stars.  
   
5. Product detail's page  
![screen shot](documentation/feat-product-detail.png)  
  * Choose the quantity and add product into the shopping bag
  * Display all the product's details including the average rating 
  * Other reviews comments and rating scores can be seen
  * Authenticated user feature
    * They can write their review and star rating
    * If wrote, user can access edit delete buttons
    ![screen shot](documentation/feat-review-modal.png)
    ![screen shot](documentation/feat-review-edit-delete.png)
  * Admin\'s Features
    * Buttons to edit and delete the product
    ![screen shot](documentation/feat-product-detail-buttons.png)
      
6. Shopping bag  
![screen shot](documentation/feat-shoppingbag.png)  
Shopping bag's function is basically same as walkthrough though, my site is using sale price as well. 
On sale product, calculated price is sale price, so I set validation to check the price is sale price or not.   
  * Button to Checkout
  * Quantity increase and decrease, or delete from bag button
  
7. Checkout
![screen shot](documentation/feat-checkout.png) 
  * Users can pay for products using credit/debit card.
    ![screen shot](documentation/feat-checkout-suc.png)
    * Users receive comfirmation emails 
    ![screen shot](documentation/feat-checkout-webhook.png) 
    * Stripe payment system  
    Now payment went through, order information is also send into Stripe. Incase of the order wasn't stored in the database, we still be able to check the order and personal information in here.
    
8. About us page  
  ![About us](documentation/feat-about.png)  
  About page is a Site owner's Greeting and/or information page that owner can create, edit and delete contents anytime using backend administrator panel.  

    * Contact form
    ![Contact form](documentation/feat-about-contact.png)  
    Site visitor can send Contanct form to this shop. Originally in my Idea, I wanted to ready these contact management functions too though, for me to complete everything in 4 weeks is really hard so those are in future feature.
9. Review page
  ![Review page](documentation/feat-review.png)  
  Review page is simply just showing the product details page's reviews collection.  What I was aiming is to show which kind of products are popular, and user can compare the product with similar charactor items. For reviewer, sharing their favorite plants might be a good opotunity to create their artistic plants life. Good decorating ideas everyone loves to see.

10. Newsletter   
![screen shot](documentation/feat-shoppingbag.png)  
We don't want to miss out on new site visitors, these pages are important.  
  if Authenticated user,  
  * Prefill user\'s registerd email address in the News Letter form
  ![screen shot](documentation/feat-newsl-send-mail.png)  
  This email is sent when applied the Newsletter. 

* Product create pages
  ![screen shot](documentation/feat-product-manage-add.gif)

* Product edit page
  ![screen shot](documentation/feat-product-manage-edit.gif)
 * User Features  
  * Toasts - 
  

### Future Features
* Newsletter unsubscribe functions is necessary
* Order management function - list page wit checkbox and details page for administrator and stuff. 
* Contact form management function - list page with checkbox and details page for administrator and stuff.
* Contact form management function - mail reply function for administrator and stuff.


## WEB MARKETING
### Ecommerce Business Model
This shopping site sells plant\'s product to individual customers ( end-users ) with single Payment so the business model is B2C ( Business to Customers ). Also this business is still small and does not have a huge marketing badjet to buy google ad slots. So the way to fit this site is to use social networking to create as many external link accesses as possible. 

Create this shop's business account in these SNS - Facebook, Twitter(X), Youtube, instagram
It is also important to update the blog and posts as often as possible and connect with as many other vendors and customers as possible. 

Newsletters must also be used effectively to keep customers who visit the site once. 
Sending too many emails too often is not a good idea from a busyness point of view, so sometimes send an atractive information for the customer.

### SEO Keywords
> Short-tail keywords are generic terms with high search volume and greater competition. For example, short-tail keywords could be ‘travel’, ‘watches’, or ‘coffee’. Long-tail keywords are nicher terms with lower search volume and less competition.   
Quoted from [SemetricalSemetrical: SEO Keywords: The Long & Short of It](https://www.semetrical.com/seo-keywords-long-tail-vs-short-tail/#:~:text=Short%2Dtail%20keywords%20are%20generic,search%20volume%20and%20less%20competition.)  

Short-tail keywords are absolutely necessary to get into the right categories, even if competition is high. So right keywords are 'Succulent', 'Succulents', 'Airplant', 'Airplants', 'Air plants', 'Indoor plants', 'house plants', 'Terarrium', 'easy care'.   
The other hand in long-tail keywords, I will aim the areas with as little competition as possible, also consider it a way to select a targeted group of customers. From my primary target users 'busy people who like easily managed plants.' One persona that I can think is an office worker who might like real greenery  in their environment. I chose these words from [Wordtracker website](https://www.wordtracker.com/search) 'low maintenance', 'easy-care plants'. 'terrarium plants', 'succulent terrarium', 'how to build a terrarium', 'interior house plants', 'interior plant maintenance'

### SNS Facebook Business Page
These SNS pages themselves are a really good advertisement, and not only that, the link connection from those live sites is important to get the main website good page ranking. 
![Facebook sample page](documentation/webm-facebook-mockup.jpg)

### Sitemap and robots.txt
I generated sitemap from [XML-Sitemaps.com ](https://www.xml-sitemaps.com/details-little-plant-shop-e08318b823f1.herokuapp.com-ee7ab3387.html)
and robots.txt
```
User-agent: *
Disallow:
Sitemap: https://little-plant-shop-e08318b823f1.herokuapp.com/sitemap.xml
```

## Testing
[Testing file - All the validation, Code and User story testings are here](/TESTING.md) 

## BUGS
### Fixed bugs

#### Path to display images in media files  
I was thinking to use the template tags to display images same-way like {{ url 'file-name' }} or {{ static 'file-name' }}.  
But those are invalid, so tried to get absolute path use template expression `{{ "media/houseplants-in-small-pots.webp" }}` it worked in my local though not in Heroku. Looking around for a while, finally I understand that the meaning we set `MEDIA_URL = "/media/"` in the settings. this is not for only template tag, I can access the variable `MEDIA_URL` even in the 
image's path.  
  
![Bug path to display image](documentation/bug-media-url.png)  
  
#### Special offer page - filtered from products  
Special offer page is the list of filtered products: field `sale_price`   
First I set the `exclude:` exclude the field value is "0" `.exclude(sale_price__icontains=0)` with default value is "0" to get the query.   
Then in admin panel, I thought the field automatically filled with "0" might make users confused, so if the product is not offered I changed the field so it can accept empty input. Changed the syntax to:`.filter(sale_price__isnull=False)` 
Then next, the product with it's sale price is "0", that is showed as not Null.   
  
![the product with it's sale price is "0", that is showed as not Null](/documentation/bug-special-offer-filtering.webp)  
I could add an another syntax after that though I found nice simple chaining in stackoverflow. In my case `.exclude(sale_price__isnull=True, sale_price__exact=0)` does not work though `.exclude(sale_price__isnull=True).exclude(sale_price__exact=0)` was successfully worked.  
  
![Stackoverflow - How to filter empty or NULL names in a QuerySet?](/documentation/bug-special-offer-filtering2-.webp)   

* Solution: Use the chaining method to get the query is not Null and not "0"  
    
### Products sorting by rating value was not working  
I was using 'PlantItem' model's function 'average_rating' to get individual value, and it's no problem until this issue came to me.  
This time I needed to get rating values for each one of instances and then sorting out.
I couldn't use the model class function to get this at all.
I found out that Django's ORM and query system work at the database level, not at the Python object level.
So my model's function works for only individual instances, not for the data in the database.

To solve this, I found the django `Subquery()` expressions.
`from django.db.models import OuterRef, Subquery`
Using this to get the average rating value from `ReviewRating` model directly.
```
# create new 'avg_rating' field in the model
products = products.annotate(
    # Subquery, OuterRef to get rating value from ReviewRating
    avg_rating=Subquery(
        ReviewRating.objects.filter(product=OuterRef('pk'))
        .values('product')
        .annotate(avg=Avg('rating'))
        .values('avg')
    )
)
```
These websites helped me to write the code.
[Django Subquery() expressions](https://docs.djangoproject.com/en/5.1/ref/models/expressions/#:~:text=Subquery%28%29%20expressions)
[How to do a subquery expression in Django?](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/subquery.html)
![Django Subquery](/documentation/credit-code-subquery1.png)
![Django ORM Cookbook](/documentation/credit-code-subquery2.png)


### Tracked BUGS
There were more bugs but I have no time to write all so please check below.
All previously closed/fixed bugs can be tracked here.  
[Project sorted by BUG](https://github.com/users/AtsukoCoffey/projects/7/views/1?filterQuery=label%3ABUG).

Fixed bugs are in `Done status` and `No status` is Unfixed bug.

### Unfixed bugs
#### BUG: Review star rating in modal - CSS issue
When first time user rated star in details page, the rating is updated though,
if reopen the edit button or create button, the stars (css) does not updated unless reload the page.
The data is no problem though the css is not working properly to show how many stars I rated before.
After reload the page those stars can display properly. 
[#55 BUG: Review star rating in modal - CSS issue](https://github.com/users/AtsukoCoffey/projects/7/views/1?filterQuery=label%3ABUG&pane=issue&itemId=99376875&issue=AtsukoCoffey%7Clittle_plant%7C55)

#### BUG: Sorting dropdown's star rating counts null or empty rate as a high score.
I have just fixed the sorting by rating value using `subquery()` though, now I found the sort is counting null or empty value wrong way. I tried to think about the solution using if statement or even using template tags though, I couldn't have good idea. If null or empty set to 0, this `subquery()` calculate all the data that didn't do reviews so the rating value becomes lower. Or if I take out the null value from the list of query and create new `product` list, I'm not sure to overide the `product` correctlly as other sortkeys will use this too.  
This is unfixed Bug. I will leave this, until next time.

## Technology used
###
* HTML, CSS used for structure my webpages and layout.
* JavaScript used for a part of the comment functionality. Programming language.
* Python used for all functionality. Programming language.
* VS code used as a local codeing soft for development.
* Git used for recording changes. A version control system.
* GitHub Used for our project's platformused for secure online code storage.
* Heroku Used for our project's platform. The deployed site.
* Django Used for our project's web framework.
* Font Awesome used for all the icons in this project.
* Google Fonts used for all the fonts used in this project and to compare potential fonts.
* Bootstrap used as the front-end CSS framework.
* PostgreSQL used as the relational database management.
* ElephantSQL used as the Postgres database.
* Psycopg2 used as a PostgreSQL database adapter.
* Stripe used for online secure payments of ecommerce.
* AWS S3 used for online static file storage.
* Django Allauth used as the user authentication system
* Pillow used as the Python framework for the site.
* Gunicorn used for WSGI server.
* Crispy Forms used for auto-formatting of front-end forms
* [RealFaviconGenerator](https://realfavicongenerator.net/) used for gemerate my favicon.
* Tinypng used for generating webp format images.

### AWS Amazon S3 settings

**Create an S3 bucket**  
--
1. Create New Bucket
2. Select `ACLs enabled` : access control lists (ACLs) 
Object ownership determines who can specify access to objects.
3. Select `Bucket owner preferred`
If new objects written to this bucket, they are owned by the bucket owner. Otherwise, they are owned by the object writer.
4. Block Public Access settings for this bucket > Deselect `Block all public access`
Turning off block all public access might result in this bucket and the objects within becoming public
5. Check the box to acknowledge the risk of public access
6. `create bucket`
* Keep ARN somewhere, we use it sometimes

**Enable static website hosting**  
--
1. In `Properties` tab `static website hosting` > `Edit`
2. Click `Enable`
3. Enter `index.html` into the Index document input
4. Enter `error.html` into the Error document input
5. `Save changes`
--


**Change CORS configuration**   
--
Permission tab :
Cross-origin resource sharing (CORS) section and click `Edit`

Add the following code for the CORS settings
```
[
    {
        "AllowedHeaders": ["Authorization"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```
`Save changes`  

**Add a bucket policy**  
--
Permissions tab:
`Bucket policy` section and click `Edit` > Click `Policy Generator`
  1. For the policy type you can select `S3 Bucket Policy`
  2. For the principal you can enter “ * ” without quotes
  3. For the Action select `GetObject` from the dropdown
  4. Then go back to copy the ARN: then the other tab to the Policy Generator
  5. Paste the ARN into the ARN input
  6. Click `Add Statement`
  7. Scroll down and click `Generate Policy`
  8. Copy all of the text in the popup:
  9. Go back to the policy editor in the other tab and paste in the policy code.
  10. Edit the `Resource` value by adding /* to the end, to allow access to all objects within the bucket
```
e.g..................
{
    "Version": "2012-10-17",
    "Id": "Policy1720032710777",
    "Statement": [
        {
            "Sid": "Stmt1720024120521",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "YOUR_ARN/*"
        }
    ]
}
```
`Save Changes`  

**Edit the Access Control List (ACL)**
--
Permissions tab:
Access control list (ACL) > `Edit`
  1. Click `List` in the Everyone (public access)
  2. Click the checkbox to indicate that you understand the effects of the changes
`Save changes`  


**Creating AWS Groups, Policies and Users - IAM Dashboard**  

**Create a user group**  
--
Search for `iam` in the search bar at the top
1. Go to `IAM`
2. Click `User Groups` on the left nav
3. Click `Create Group`
4. Enter a group name: (manage-little-plant-shop)
`Create user group`  

**Create a Policy**  
--
`Policies` in the left nav > `Create Policy`
1. Click the `JSON` tab
2. Click the `Actions` dropdown
3. Click `Import policy`
4. Search for `s3`
5. Select `AmazonS3FullAccess`
6. Click `Import Policy`
7. Ready and copy `ARN' 

8. Add your ARN in quotes to the `Resource` list twice, one with /* after the ARN.
```
e.g..................
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
            "YOUR_ARN",
            "YOUR_ARN/*"
            ]
        }
    ]
}
```
9. `Next`
10. Enter a policy name and description
11. `Create policy`  


**Attach the policy to the group  - IAM Dashboard**  
--
1. `User groups` in the left nav
2. Click your group to go Summary page
3. `Permissions` tab
4. `Add permissions` dropdown
5. `Attach policies
6. Search for your policy
7. `Attach policies`  


**Create a User  - IAM Dashboard**  
--
1. `Users` in the left nav
2. `Create user`
3. Enter a user name
4. Select the group you created previously
6. `Create user`  


**Create an Access Key - IAM Dashboard**  
--
1. Select the new user
2. `Security credentials` tab
3. `Access keys` section > click `Create access key`
4. Select `Application running outside AWS` > `Next`
5. `Create access key`:
1. Download .csv file > `Done`  


**AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY**  
--
* Values are separated by a comma `,`  
AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

**Install Boto3, django-storages and settings**  
-- 
1. To connect django to S3 we need these packages`pip3 install boto3`, `pip3 install django-storages`  
2. Freeze those `pip3 freeze --local > requirements.txt` and add `django-storages` to `INSTALLED_APPS`
3. Specify details of which S3 backets to connect to.
```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'little-plant-shop'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
4. In Heroku config delete `DISABLE_COLLECTSTATIC` add these variables  
* `USE_AWS`: `True`
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`  

5. Create `custom_storates.py`   
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
When this is deployed, Heroku will run `python3 manage.py collectstatic` during the build process. 
Static files will be collected into a static folder in our s3 bucket.  

6. For media files, create media folder in AWS and give public permission and upload the images.
Add cache control in AWS settings  
```
# Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```




## CREDIT
### Learning material
* CodeInstitute LMS
All the basics from the understanding what Django is to how to use it. Also everything that I learned about python and code.


### Credit - Contents

I borrowed all the products from these web sites. 
* House plant and succulents were from 'Gardens4you' [https://www.gardens4you.ie/](https://www.gardens4you.ie/)
* Air plants were from 'PlantStore.ie' [https://www.plantstore.ie/](https://www.plantstore.ie/)

I couldn't find private pictures for review, so I borrowed from these web site. A little bit professional than people's reviews though, those are as sample pictures.
* For reviews pictures from 'save on crafts' [https://www.save-on-crafts.com/](https://www.save-on-crafts.com/) 

FAQ contents
* How to care Air plants [Gardeners World com - A complete guide to caring for air plants](https://www.gardenersworld.com/how-to/grow-plants/air-plants-tillandsia/)
* [AIR PLANT DESIGN STUDIO - Basic Care](https://www.air-plants.com/pages/frequently-asked-questions-tillandsia)
* [PATCH - Complete guide to succulent care](https://www.patchplants.com/pages/plant-care/complete-guide-to-succulent-care/)
* [Better Homes & Gardens - 10 Indoor Plant Care Tips to Ensure Happy, Healthy Houseplants](https://www.bhg.com/gardening/houseplants/care/houseplant-care-guide/)
* [Pilea - 10 Common Questions About Houseplants Answered](https://www.pilea.com/post/10-common-questions-about-houseplants-answered)
* [GARDEN SHOP.ie - FAQ](https://www.thegardenshop.ie/faqs/)
* Terrarium [greeneryunlimited - Frequently Asked Questions](https://greeneryunlimited.co/pages/terrarium-faq?srsltid=AfmBOooeMlHb9QwWAYFO2sCVwFIFqJ_C4J-9589TqA6cn3W_V5JNOatq)

About us page
* [freepik material](https://www.freepik.com/free-photo/beautiful-young-woman-flower-shop-choosing-flowers_9495440.htm#fromView=search&page=1&position=0&uuid=345383e2-ca05-4ad7-9083-67897be2759f&query=Plant+shop+succulent)

 

### Credit - images
* Hero image - Unsplash (Free image website)  
[purple green succulents pic](https://unsplash.com/photos/purple-and-green-succulent-plant-Hs1B-3N-WQg)

* About us picture - Lovely girl with succulents
[Lovely girl with succulents](https://www.freepik.com/free-photo/beautiful-young-woman-flower-shop-choosing-flowers_9495440.htm#fromView=search&page=1&position=0&uuid=345383e2-ca05-4ad7-9083-67897be2759f&query=Plant+shop+succulent)

* I borrowed all the products from these web sites.   
House plant and succulents were from Gardens4you [https://www.gardens4you.ie/](https://www.gardens4you.ie/)
Air plants were from PlantStore.ie [https://www.plantstore.ie/](https://www.plantstore.ie/)

* For reviews pictures, I couldn't find private pictures so I borrowed from save on crafts    
[https://www.save-on-crafts.com/](https://www.save-on-crafts.com/) web site. A little bit professional than people's reviews though, those are as sample pictures.


* [Air plant and succulent plant](https://greengardencottage.com/wp-content/uploads/2023/02/air-plants-verses-succulents-1024x765.jpg)
* [Air plant and succulent plant used top page](https://www.sucasamagazine.com/wp-content/uploads/2021/12/succulents-and-air-plants-in-terrarium.jpg)


* [SheCodes - [JavaScript] - How to create an Accordion with JavaScript](https://www.shecodes.io/athena/9202-how-to-create-an-accordion-with-javascript)

### ACKNOWLEDGEMENTS
I would like to give great thanks to my mentor Gareth Mc Girr.
Also my cohort facilitator Lewis Dillon for all the support and assistance.   
And great thanks to my family Sean Coffey and children for all the support.