# Testing

## Code Validation

### HTML
| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2F) | ![screenshot](documentation/vali-html-top.png) | No Error |
| Sign-up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/vali-html-signup.png) | No Error |
| Log-in | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/vali-html-login.png) | No Error ||
| Log-out | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhealthy-food-c44b0f8f09a5.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](documentation/vali-html-logout.png) | No Error |
| Products list | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/vali-html-products.png) | No Error |
| Products detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2Fpachyveria-corvus) | ![screenshot](documentation/vali-html-detail.png) | No Error |
| FAQ | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Ffaq%2F%3Fcategory%3D1) | ![screenshot](documentation/vali-html-faq.png) | No Error |
| Reviews | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fproducts%2Freview%2F) | ![screenshot](documentation/vali-html-review.png) | No Error |
| About us | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/vali-html-about.png) | No Error |
| Shopping bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fbag%2F) | ![screenshot]() | Error |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fcheckout%2F) | ![screenshot]() | Error |
| Checkout success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Flittle-plant-shop-e08318b823f1.herokuapp.com%2Fcheckout%2Fcheckout_success%2FA3CEB167CDEA4CAA8BC9A6F35FFB6440) | ![screenshot]() | No Error |
| Profile | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot](documentation/vali-html-profile.png) | Error |
| Newsletter | [W3C - Validated By Input]() | ![screenshot](documentation/vali-html-newsletter.png) | No Error |
| Privacy Policy | [W3C - Validated By Input](https://validator.w3.org/#validate_by_input) | ![screenshot]() | Error |
--

### CSS
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flittle-plant-shop.s3.eu-west-1.amazonaws.com%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot]() |  |

### JavaScript
| File | Screenshot | Notes |
| --- | --- | --- |
| static/product-functions.js | ![screenshot](documentation/vali-jshint-root-js.png) | --- |
| checkout/stripe_elements.js | ![screenshot](documentation/vali-jshint-checkout-stripe.png) | --- |
| --- | --- | --- |

### Python

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

### PC Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/vali-light-top-d.png) |  |
| Product list | Desktop | ![screenshot](documentation/vali-light-products-d.png) |  |
| Product detail | Desktop | ![screenshot](documentation/vali-light-detail-d.png.png) |  |
| FAQ | Desktop | ![screenshot](documentation/vali-light-faq-d.png) |  |
| Reviews | Desktop | ![screenshot](documentation) |  |
| About us | Desktop | ![screenshot](documentation/vali-light-about-d.png) |  |
| Privacy policy | Desktop | ![screenshot](documentation/vali-light-) |  |
| Profile | Desktop | ![screenshot](documentation/vali-light-profile-d.png) |  |
| Profile success | Desktop | ![screenshot](documentation) |  |

| Product add | Desktop | ![screenshot](documentation/va) |  |
| Product edit | Desktop | ![screenshot](documentation) |  |
| Shopping bag | Desktop | ![screenshot](documentation) |  |

| Check out | Desktop | ![screenshot](documentation) |  |
| Check out success | Desktop | ![screenshot](documentation) |  |

* error details
![Error](documentation/vali-light-error-link-no-crawl.png)  



### Mobile Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/vali-light-top-m.png) |  |
| Product list | Mobile | ![screenshot](documentation/vali-light-products-m.png) |  |
| Product detail | Mobile | ![screenshot](documentation/vali-light-detail-m.png) |  |
| FAQ | Mobile | ![screenshot](documentation) |  |
| Reviews | Mobile | ![screenshot](documentation) |  |
| About us | Mobile | ![screenshot](documentation) |  |
| Privacy policy | Mobile | ![screenshot](documentation/vali-light-) |  |
| Profile | Mobile | ![screenshot](documentation/vali-light-profile-m.png) |  |
| Profile success | Mobile | ![screenshot](documentation) |  |

| Product add | Mobile | ![screenshot](documentation/va) |  |
| Product edit | Mobile | ![screenshot](documentation) |  |
| Shopping bag | Mobile | ![screenshot](documentation) |  |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Home Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | Click on Logo | Redirection to Home page | Pass | |
| | Click on Profile icon in navbar  | Display dropdown list | Pass | |
| | Click on Register | Redirection to Sign in page | Pass | |
| | Click on Login | Redirection to Login page | Pass | |
| | Click on Product management | Redirection to Product add page | Pass | |
| | Click on My profile | Redirection to Profile page | Pass | |
| | Click on Logout | Redirection to Logout page | Pass | |
| | Click on Bag icon  | Redirection to shopping bag page | Pass | |
| | Hover on links  | shows hover color | Pass | |
| Authenticated user only | under the profile icon | User name is displayed under | Pass | |
| | Click on SHOP PLANTS | Display dropdown list | Pass | |
| | Click on All Products | Redirection to products page | Pass | |
| | Click on each category name | Filtered products with each category | Pass | |
| | Click on SPECIAL OFFER | Filtered with sale_price has valid price | Pass | |
| | Click on FAQ | Display dropdown list | Pass | |
| | Click on FAQ each category | Filtered FAQ with each category | Pass | |
| | Click on REVIEWS  | Display dropdown list | Pass | |
| | Click on REVIEWS All Products | Redirection to Review page | Pass | |
| | Click on REVIEWS each category | Filtered with each category | Pass | |




## User story Testing
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