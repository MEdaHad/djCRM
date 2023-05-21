# CRM with Django
This project is a customer relationship management (CRM) system built using Django. It allows you to manage leads and clients, convert leads to clients, and process payments using Stripe.

## Features
User authentication: Allows team members to log in and access the CRM.

   1 . Simple dashboard: Displays key metrics and information about leads and clients. 

   2 . Lead management: Create, change, and delete leads.

   3 . Client management: Create, change, and delete clients.
   
   4 . Conversion of leads to clients: Easily convert leads to clients.
   
   5 . Payment solutions: Monthly recurring payments through Stripe.
   
   6 . Team management: Add, change, and delete team members.
   
   7 . Security: Sensitive information, such as payment details, is stored securely.

## Installation and Setup
   1 .Clone the repository to your local machine.

   2 .Create a virtual environment and activate it.

   3 .Install the required dependencies using pip install -r requirements.txt.

   4 .Set up the database by running python manage.py migrate.

   5 .Set up the database by running python manage.py migrate.

   6 .Set up the database by running python manage.py migrate.

   7 .Create a superuser account using python manage.py 
   createsuperuser.

   8 .Start the development server using python manage.py 
   runserver.

## Configuration
The following environment variables need to be set:

   . SECRET_KEY: Django secret key.
   . DATABASE_URL: URL of the database.
   . STRIPE_SECRET_KEY: Stripe secret key.
   . STRIPE_PUBLISHABLE_KEY: Stripe publishable key.
## Contributing
   1 .Fork the repository and create a new branch.

   2 .Make your changes and commit them.

   3 .Create a pull request.

