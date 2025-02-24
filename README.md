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
My planning diagram was below, then I found some missing models on the way.  
![Database relationship diagram](documentation/db-diagram.webp "Database relationship diagram")  
Finally models became like this.  
![Database relationship diagram](documentation/db-diagram02.png "Database relationship diagram") 

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

### Surface

#### Fonts
* Handlee  

#### Colour scheme 
![Colour scheme](documentation/colour-scheme.png "Colour scheme")  

## FEATURES  

### Existing Features 
#### Site Pages

1. Homepage  
  * Navigation bar
  * Login Dependant Account links
  * Product\'s search bar
  * Some recomended contents in the Bootstrap\'s carousel
  * Newsletter Registeration
  * Display account authentication status
  * Logged-in user\'s only  
    * Access link to profile page
    * Prefill user\'s registerd email address in the News Letter form
  * Admin\'s Features  
    * Add a new plant product
    * Link to Order manage page
    * Link to Contact query manage page
2. Authetication pages
  * User Registration
  * User Login
  * User Logout
3. Profile page
4. Product list view page
  * Ordered by name, price and search 
5. Product detail's page
  * Add in the shopping bag
  * reviews and star rating scores
  * Admin\'s Features
    * Buttons to edit and delete the product
6. Shopping bag
  * Button to Checkout
7. Checkout
  * Users can payfor products using credit/debit card.
  * Users receive comfirmation emails 
8. About us page
  * Contact form
9. Review page

* Other pages
 * User Features  
   * Authentication Password reset
   * Toasts - 

### Future Features

![Checkout Webhook](documentation/feat-checkout-webhook.png)
![Checkout Webhook](documentation/feat-newsl-send-mail.png)
![Checkout Webhook]()

## WEB MARKETING
### Ecommerce Businness Model
This shopping site sells plant\'s product to individual customers ( end-users ) with single Payment so the businness model is B2C ( Bussiness to Customers ).

Newsletter registration, Facebook and other SNS links

## Testing

### Code Validation

#### HTML
| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2F) | ![screenshot]() | Error |
| Sign-up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot]() | Error |
| Log-in | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot]() | Error ||
| Log-out | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhealthy-food-c44b0f8f09a5.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot]() | Error |
| Products list | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2F) | ![screenshot]() | Error |
| Products detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2Fpachyveria-corvus) | ![screenshot]() | Error |
| FAQ | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Ffaq%2F%3Fcategory%3D1) | ![screenshot]() | Error |
| Reviews | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2Freview%2F) | ![screenshot]() | Error |
| About us | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fabout%2F) | ![screenshot]() | Error |
| Shopping bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fbag%2F) | ![screenshot]() | Error |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fcheckout%2F) | ![screenshot]() | Error |
| Checkout success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fcheckout%2Fcheckout_success%2FA3CEB167CDEA4CAA8BC9A6F35FFB6440) | ![screenshot]() | No Error |
| Profile | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| Newsletter | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| Privacy Policy | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |


| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
| page | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |

#### CSS
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flittle-plant-shop.s3.eu-west-1.amazonaws.com%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot]() |  |

#### JavaScript
| File | Screenshot | Notes |
| --- | --- | --- |
| static/product-functions.js | ![screenshot](documentation/vali-jshint-root-js.png) | --- |
| checkout/stripe_elements.js | ![screenshot](documentation/vali-jshint-checkout-stripe.png) | --- |
| --- | --- | --- |

#### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.  
**Project config**
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| asgi.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-config-asgi.png) | No Error |
| settings.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-config-settings.png) | No Error |
| urls.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-config-urls.png) | No Error |
| wsgi.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-config-wsgi.png) | No Error |  

**About us App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-admin.png) | no Error |
| apps.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-apps.png) | No Error |
| forms.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-forms.png) | No Error |
| models.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-models.png) | No Error |
| urls.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-urls.png) | No Error |
| views.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-about-views.png) | No Error |

**Bag App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| apps.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-bag-apps.png) | Error |
| contexts.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-bag-contexts.png) | Error |
| urls.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-bag-urls.png) | Error |
| views.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-bag-views.png) | Error |
| templatetags/bag_tools.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-bag-tag-tools.png) | Error |


**Checkout App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-admin.png) | Error |
| apps.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-apps.png) | Error |
| forms.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-forms.png) | Error |
| models.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-models.png) | Error |
| signals.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-signals.png) | Error |
| urls.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-urls.png) | Error |
| views.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-views.png) | Error |
| webhook_handler.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-wh-handler.png) | Error |
| webhooks.py | [PEP8 CI] | ![screenshot](documentation/vali-pep8-checkout-wh.png) | Error |

**FAQ App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot]() | Error |
| apps.py | [PEP8 CI] | ![screenshot]() | Error |
| models.py | [PEP8 CI] | ![screenshot]() | Error |
| urls.py | [PEP8 CI] | ![screenshot]() | Error |
| views.py | [PEP8 CI] | ![screenshot]() | Error |

**Home App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot]() | Error |
| apps.py | [PEP8 CI] | ![screenshot]() | Error |
| models.py | [PEP8 CI] | ![screenshot]() | Error |
| urls.py | [PEP8 CI] | ![screenshot]() | Error |
| views.py | [PEP8 CI] | ![screenshot]() | Error |

**Newsletter App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot]() | Error |
| apps.py | [PEP8 CI] | ![screenshot]() | Error |
| forms.py | [PEP8 CI] | ![screenshot]() | Error |
| models.py | [PEP8 CI] | ![screenshot]() | Error |
| urls.py | [PEP8 CI] | ![screenshot]() | Error |
| views.py | [PEP8 CI] | ![screenshot]() | Error |

**Products App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot]() | Error |
| apps.py | [PEP8 CI] | ![screenshot]() | Error |
| forms.py | [PEP8 CI] | ![screenshot]() | Error |
| models.py | [PEP8 CI] | ![screenshot]() | Error |
| urls.py | [PEP8 CI] | ![screenshot]() | Error |
| views.py | [PEP8 CI] | ![screenshot]() | Error |
| widgets.py | [PEP8 CI] | ![screenshot]() | Error |  

**Profile App**  
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |  
| admin.py | [PEP8 CI] | ![screenshot]() | Error |
| apps.py | [PEP8 CI] | ![screenshot]() | Error |
| forms.py | [PEP8 CI] | ![screenshot]() | Error |
| models.py | [PEP8 CI] | ![screenshot]() | Error |
| urls.py | [PEP8 CI] | ![screenshot]() | Error |
| views.py | [PEP8 CI] | ![screenshot]() | Error |

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | 
| custom_storages.py | [PEP8 CI] | ![screenshot]() | Error |

## Browser Compatibility

I've tested my deployed project on multiple browsers.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot]() | Errors |
| Firefox | ![screenshot]() | Errors |
| Edge | ![screenshot]() | Errors |
| Safari | ![screenshot]() | Errors |
| Opera | ![screenshot]() | Errors |  

## Responsiveness

I've tested my deployed project on multiple devices.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile | ![screenshot]() | Errors | 
| Tablet (DevTools) | ![screenshot]() | Errors | 
| Laptop 16" | ![screenshot]() | Errors | 
| Desktop 21.5" | ![screenshot]() | Errors | 
| 4K Monitor 40" | ![screenshot]() | Errors |   

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool.

### Mobile Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot]() | warnings |
| Product list | Mobile | ![screenshot]() | warnings |
| Product detail | Mobile | ![screenshot]() | warnings |



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
--  

# Tachnology to use
## AWS Amazon S3 settings

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

# BUGS
## Special offer page - filtered from products
Special offer page is the list of filtered products: field `sale_price`   
Firsr I set the èxclude: exclude the field value is "0" `.exclude(sale_price__icontains=0)` with default value is "0" to get the query. Then in admin panel, I thought the field automatically filled with "0" might make users confused, so if the product is not on offered I changed the field can be accepted empty input. Chenge the syntax to:`.filter(sale_price__isnull=False)` 
Then next, the product with it's sale price is "0", that is showed as not Null.  
![the product with it's sale price is "0", that is showed as not Null](/documentation/bug-special-offer-filtering.webp)  
I could add an another syntax after that though I found nice simple chaining in stackoverflow. In my case `.exclude(sale_price__isnull=True, sale_price__exact=0)` does not work though `.exclude(sale_price__isnull=True).exclude(sale_price__exact=0)` was successfully worked.
![Stackoverflow - How to filter empty or NULL names in a QuerySet?](/documentation/bug-special-offer-filtering2-.webp)   

* Solution: Use the chaining method to get the query is not Null and not "0"

## Path to display images in media files
I was thinking to use the template tags to display images same-way like {{ url 'file-name' }} or {{ static 'file-name' }}.
But those are invalid, so tried to get absolute path use template expression `{{ "media/houseplants-in-small-pots.webp" }}` it worked in my local though not in Heroku. Looking around for a while, finally I understand that the meaning we set `MEDIA_URL = "/media/"` in the settings. this is not for only template tag, I can access the variable `MEDIA_URL` even in the 
image's path. 
![Bug path to display image](documentation/bug-media-url.png)


# CREDIT
## Credit - Contents
* How to care Air plants  
> [Gardeners World com - A complete guide to caring for air plants](https://www.gardenersworld.com/how-to/grow-plants/air-plants-tillandsia/)
* [AIR PLANT DESIGN STUDIO - Basic Care](https://www.air-plants.com/pages/frequently-asked-questions-tillandsia)

* [PATCH - Complete guide to succulent care](https://www.patchplants.com/pages/plant-care/complete-guide-to-succulent-care/)
* [Better Homes & Gardens - 10 Indoor Plant Care Tips to Ensure Happy, Healthy Houseplants](https://www.bhg.com/gardening/houseplants/care/houseplant-care-guide/)
* [Pilea - 10 Common Questions About Houseplants Answered](https://www.pilea.com/post/10-common-questions-about-houseplants-answered)
* [GARDEN SHOP.ie - FAQ](https://www.thegardenshop.ie/faqs/)


* Terrarium
* [greeneryunlimited - Frequently Asked Questions](https://greeneryunlimited.co/pages/terrarium-faq?srsltid=AfmBOooeMlHb9QwWAYFO2sCVwFIFqJ_C4J-9589TqA6cn3W_V5JNOatq)

## Credit - images
* About us picture
[https://www.freepik.com/premium-photo/asian-man-gardener-caring-houseplant-flowers-greenhouse-garden-male-plant-shop-owner-working-spraying-water-potted-plants-store-small-business-entrepreneur-plant-caring-concept_399144362.htm](https://www.freepik.com/premium-photo/asian-man-gardener-caring-houseplant-flowers-greenhouse-garden-male-plant-shop-owner-working-spraying-water-potted-plants-store-small-business-entrepreneur-plant-caring-concept_399144362.htm)

* [Air plant and succulent plant](https://greengardencottage.com/wp-content/uploads/2023/02/air-plants-verses-succulents-1024x765.jpg)
* [Air plant and succulent plant used top page](https://www.sucasamagazine.com/wp-content/uploads/2021/12/succulents-and-air-plants-in-terrarium.jpg)


* [SheCodes - [JavaScript] - How to create an Accordion with JavaScript](https://www.shecodes.io/athena/9202-how-to-create-an-accordion-with-javascript)


* []()
* []()
* []()
* []()
* []()
