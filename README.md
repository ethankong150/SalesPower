<br>________________________________________________________________________________________________

## SalesPower Overview:

SalesPower is a tool to better connect customers with the retail stores they buy from and the brands that supply the products!

Currently, there are issues for customers to find the best deals for products they want to buy. Often times, different retail stores and the brand themselves will price the same product differently, whether that is due to a coupon or not. SalesPower aims to create a simpler universal coupon system that allows users a simple comparison interface between the various vendors and brands, allowing for customers to get the best deals!


### SalesPower Application details:

The application is split into seven pages. The first page serves as a landing page to send the user to the correct login portal. So if the user is a 'Customer', they'll be sent to the customer login page. And if the user is a brand employee, they'll be sent to the brand employee login page. 

#### Login Pages:
Having the types of users be sent to different login pages allows the various login pages to have differing GET requests to authenticate the users login information as the customer, retial meployee, and brand employee login information is all stored in separate tables. 

#### Customer Page:
After the customer's login informatino is confirmed, they are sent to the customer page, where they'll be to able to see a table of active coupons and the terms/details of each coupon. We used another GET request to view all of the coupons currently in the database. Below the coupon display is a form that authenticates the user once again. This is to send the user to a page to allow the customer to edit their address information, email, password etc. Again, we use a GET request to authenticate the user's login information.

#### Brand Page:
Currently, the only functionality of a Brand Employee is to add new coupons to the coupon database. To do this, the employee fills out the form and submits the new coupon. The coupon is added to the database via a POST request.

#### Retail Page:
The current functionalities of a Retial Employee include adding coupons, removing coupons, and viewing coupons. To add a coupon, the retail employee, like the brand employee, fills out the form and the information is sent to the database via POST request. To remove a coupon, the retail employee submits the CouponID into the form and the coupon is removed from the database via a DELETE request. And just like the customer page, the retail employee can view the coupons using a GET request. 
