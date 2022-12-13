CREATE DATABASE salespower;
GRANT ALL PRIVILEGES ON salespower.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE salespower;

CREATE TABLE brands (
    companyName VARCHAR(40) PRIMARY KEY,
    supportEmail VARCHAR(40) UNIQUE NOT NULL,
    phone_num CHAR(10) UNIQUE,
    postal_code CHAR(5) NOT NULL,
    state_abbr CHAR(2) NOT NULL,
    city text NOT NULL,
    street_address text NOT NULL
);

INSERT INTO brands
VALUES ('Nike', 'support@nike.com', 8003446453, 10001, 'NY', 'New York', '855 6th Ave'),
       ('Adidas', 'support@adidas.com', 8009829337, 97217, 'OR', 'Portland', '5055 N Greely Ave'),
       ('Under Armour', 'support@ua.com', 4104682512, 21230, 'MD', 'Baltimore', '1020 Hull St'),
       ('GalaxySneakers', 'support@galaxy.com', 1234567890, 02116, 'MA', 'Boston', '10 Huntington Ave');

CREATE TABLE retailoutlets (
    id integer PRIMARY KEY,
    storeNum integer,
    storeName text,
    postal_code CHAR(5) NOT NULL,
    state_abbr CHAR(2) NOT NULL,
    city text NOT NULL,
    street_address text NOT NULL
);

INSERT INTO retailoutlets
VALUES (1, 1, 'Dicks Sporting Goods', 12345, 'TX', 'Austin', '19 Jackson Lane'),
       (2, 1, 'Foot Locker', 54321, 'CA', 'Sacramento', '5 Kings Bl'),
       (3, 1, 'Target', 67890, 'MN', 'Minneanapolis', '32 Wolves Court'),
       (4, 2, 'Dicks Sporting Goods', 09876, 'OK', 'Oklahoma City', '2 Thunder Dr'),
       (5, 2, 'Foot Locker', 39043, 'AZ', 'Phoenix', '1 Suns Road');

CREATE TABLE customers (
    customerID integer PRIMARY KEY,
    email VARCHAR(40) UNIQUE NOT NULL,
    phone_num CHAR(10),
    postal_code CHAR(5) NOT NULL,
    state_abbr CHAR(2) NOT NULL,
    city text NOT NULL,
    street_address text NOT NULL,
    f_name text NOT NULL,
    l_name text NOT NULL,
    pass text NOT NULL
);

INSERT INTO customers
VALUES (1, 'lebronjames@gmail.com', 2362362360, 12345, 'CA', 'Los Angeles', '17 Crypto Arena', 'LeBron', 'James', 'lakers'),
       (2, 'anthonydavis@gmail.com', 2332332330, 12345, 'CA', 'Los Angeles', '17 Crypto Arena', 'Anthony', 'Davis', 'center'),
       (3, 'russellwestbrick@gmail.com', 0000000000, 12345, 'CA', 'Los Angeles', '17 Crypto Arena', 'Russell', 'Westbrook', 'badplayer'),
       (4, 'rjbarrett@gmail.com', 5959595900, 67890, 'NY', 'New York', '2 Garden Arena', 'RJ', 'Barrett', 'duke'),
       (5, 'juliusrandle@gmail.com', 3030303030, 67890, 'NY', 'New York', '2 Garden Arena', 'Julius', 'Randle', 'knicks'),
       (6, 'camreddish@gmail.com', 2102102100, 67890, 'NY', 'New York', '2 Garden Arena', 'Cam', 'Reddish', 'who');

CREATE TABLE products (
    productID integer PRIMARY KEY,
    productName text NOT NULL,
    unitPRICE integer NOT NULL,
    quantityInStock integer NOT NULL
);

INSERT INTO products
VALUES (1000, 'Panda', 100, 50), (1001, 'Red Panda', 100, 25), (2000, 'UltraBoost', 80, 1000), (3000, 'Curry 5', 200, 2000);

CREATE TABLE orders (
    orderID integer PRIMARY KEY,
    orderDATE CHAR(8) NOT NULL,
    productID integer NOT NULL,
    customerID integer NOT NULL
);

INSERT INTO orders
VALUES (101, '11/1/22', 1000, 1), (102, '11/2/22', 1001, 2), (103, '11/3/22', 2000, 3), (104, '11/4/22', 3000, 4),
       (105, '11/5/22', 1000, 5), (106, '11/6/22', 1001, 6);

CREATE TABLE suppliessells (
    companyName VARCHAR(40) NOT NULL,
    productID integer NOT NULL,
    PRIMARY KEY (companyName, productID)
);

INSERT INTO suppliessells
VALUES ('Nike', 1000), ('Nike', 1001), ('Adidas', 2000), ('Under Armor', 3000);

CREATE TABLE sells (
    retail_outlet_id integer NOT NULL,
    productID integer NOT NULL,
    PRIMARY KEY (retail_outlet_id, productID)
);

INSERT INTO sells
VALUES (1, 1000), (1, 2000), (2, 1000), (2, 3000), (3, 1000), (4, 3000);

CREATE TABLE brandemployee (
    employeeID integer PRIMARY KEY,
    email text NOT NULL,
    title text NOT NULL,
    f_name text NOT NULL,
    l_name text NOT NULL,
    postal_code CHAR(5) NOT NULL,
    state_abbr CHAR(2) NOT NULL,
    city text NOT NULL,
    street_address text NOT NULL,
    pass text NOT NULL
);

INSERT INTO brandemployee
VALUES (9999, 'john@gmail.com', 'administration', 'john', 'cena', 49494, 'OH', 'Canton', '23 King Road', 'password'),
       (9998, 'jeff@yahoo.com', 'retail relationships', 'jeff', 'van gundy', 39393, 'NV', 'Las Vegas', '6 Poker Lane', 'secret');

CREATE TABLE brandemploys (
    companyName VARCHAR(40) NOT NULL,
    storeEmployeeID integer NOT NULL,
    PRIMARY KEY (companyName, storeEmployeeID)
);

INSERT INTO brandemploys
VALUES ('Nike', 9999), ('Adidas', 9998);

CREATE TABLE outletemployee (
    employeeID integer PRIMARY KEY,
    email text NOT NULL,
    title text NOT NULL,
    f_name text NOT NULL,
    l_name text NOT NULL,
    postal_code CHAR(5) NOT NULL,
    state_abbr CHAR(2) NOT NULL,
    city text NOT NULL,
    street_address text NOT NULL,
    pass text NOT NULL
);

INSERT INTO outletemployee
VALUES (1000, 'jane@gmail.com', 'administration', 'jane', 'doe', 49494, 'NJ', 'Plainsboro', '9 Young Bl', 'admin'),
       (1001, 'jodie@yahoo.com', 'retail relationships', 'jodie', 'brown', 39393, 'WY', 'Jackson Hole', '8 Hohman Court', '123456789');

CREATE TABLE retailemploys (
    companyName VARCHAR(40) NOT NULL,
    storeEmployeeID integer NOT NULL,
    PRIMARY KEY (companyName, storeEmployeeID)
);

INSERT INTO retailemploys
VALUES (1, 1000), (2, 1001);

CREATE TABLE coupon (
    couponID integer PRIMARY KEY,
    terms text NOT NULL,
    endDate text NOT NULL
);

INSERT INTO coupon
VALUES (1, '75% off', '01/01/2023'), (2, '50% off', '01/01/2023');

CREATE TABLE discount (
    couponID integer NOT NULL,
    productID integer NOT NULL,
    PRIMARY KEY (couponID, productID)
);

INSERT INTO discount
VALUES (1, 1000), (2, 1001);