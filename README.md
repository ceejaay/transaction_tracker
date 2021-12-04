# Transaction Tracker

Transaction tracker is a simple api that keeps track of User, Merchants and Transactions. Users and Merchants are
independent of one another in this version. Transactions belong to a user and belong to a merchant. With these endpoints
you can create, delete, and update Users and Merchants. In this version you can create Transactions with a valid user id
and a valid merchant id. Finally you can get a list of transactions by both Merchant and Users.

### Libraries
* Flask: As a lightweight framework.
* Flask-sqlalchemy: A library to connect to a sql database.
* Marshmallow: Creates and manages schemas for the models and the database.
* flask-restful: Manages the app's endpoint URLs

### Users
Users have these properties.
* first_name: string
* last_name: string
* dob: string
* inserted_at: datetime
* updated_at: datetime


### User endpoints.

1. Create a user
    * POST to `/api/v0/users`
2. Get all users
    * GET to `/api/v0/users`
3. Get, delete, or update a single user.
    * GET, DELETE, PATCH to `/api/v0/users/<user id>`

### Merchants
Merchants have these properties.
* name: string
* description: string

### Merchant endpoints 
1. Create a merchant 
    * POST to `/api/v0/merchants`
2. Get all merchants 
    * GET to `/api/v0/merchants`
3. Get, delete, or update a single merchant.
    * GET, DELETE, PATCH to `/api/v0/merchants/<merchant id>`

### Transactions 
Transactions have these properties.
* description: string
* amount: integer

### Transaction relationships
* user_id: and existing user id
* merchant_id: and existing merchant id



### Trnsaction endpoints 
1. Create a transaction 
    * POST to `/api/v0/transactions/users/< user id>/merchants/<merchant id>`


### Transactions by Merchant or User

1. By User
    * GET to `/api/v0/users/<user id>/transactions`
2. By Merchant 
    * GET to `/api/v0/merchants/<merchants id>/transactions`

### Todo
- Refactor the code structure to break up the App file. For improved readability
-  Add DELETE function to Transactions.
- Add PATCH function to Transactions
- Create a Company model that has a relationship with users and transactions.
