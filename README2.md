# UCI Enduro World Cup Management System


## Features

- **Rider Management**: Create and view detailed profiles for each rider, including race results.
- **Race Results**: Display qualifying and final race results in real-time.
- **Race Order Management**: Automatically generate race start orders based on qualifying results.
- **Podium Results**: Show top performers in each age category.
- **Dynamic Searching**: Filter riders by name, team, or age category through an AJAX-enabled interface.

## Setup Instructions
Set up a Python Virtual Environment
python -m env env

**Install Dependencies**
pip install -r requirements.txt


**Initialize the Database**
python manage.py makemigrations
python manage.py migrate

**create super user to have access to all CRUD**
Create an Admin User
python manage.py createsuperuser
USE THE DJANGO ADMIN TO HAVE ACCESS TO ALL THE NEEDED DATA

**Run the Development Server**
python manage.py runserver
Visit http://127.0.0.1:8000/rider/ in your web browser.

Usage
The project includes several URL routes that provide access to its features:

/riders/ - List all riders.

/riders/<int:pk>/ - Detailed view of a single rider's profile and results.

/qualifying/ - View a list of riders sorted by qualifying times.

/race_order/ - View the start order for the race based on qualifying results.

/register/ - Register a new rider into the system.

/podium/ - View podium results by age category.

**TO TEST, RUN THE BEOLW COMMAND**
 python manage.py test world_cup.tests


**ADDITIONAL FEATURES**
WORK PERFECTLY WITH DOCKER AND DOCKER COMPOSE
This application provides a JSON API for dynamically searching and filtering riders which responds to AJAX requests at:
/riders/ with parameters for search and age category.