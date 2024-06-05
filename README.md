# 'News'  

'News'  - Django web app for managing parsed articles from different sources.

## Required Python packages
Mandatory Python packages
- Django
- python-dotenv


## Project setup process


#### 1. Activate a new virtual environment:
- **_Create virtual environment._**\
Script below is creating environment with name 'env'.\
If you want to create environment with unique name, please replace the env name using your env name in script\
_python -m {here_is_your_venv_name} ../env_\
 <br />Working script for creating venv with name 'venv' is below:\
a. `python -m venv ../env`\
then activate it\
b. `source ../venv/bin/activate`
or \
`python -m venv venv_for_news_project`\
and then\
`source venv_for_news_project/Scripts/activate`

#### 2. Install packages:

`pip install --upgrade pip`\
then\
`pip install -r requirements.txt`\
If **_requirements.txt_** file is missing request, or you have different configuration of the project, please  generate a file using command\
`pip freeze > requirements.txt` \
and add it into the root folder of the project.

### 2. Install Django

- Django installation (manual installation via **_pip_**)

  * Windows `pip install django`
  * Mac `python -m pip install Django`

#### 2. Migrate DB
 *Migrations* are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

*The Commands*\
There are several commands which you will use to interact with migrations and Django’s handling of database schema:\
- _**migrate**_, which is responsible for applying and unapplying migrations.
- **_makemigrations_**, which is responsible for creating new migrations based on the changes you have made to your models.
sqlmigrate, which displays the SQL statements for a migration.
- **_showmigrations_**, which lists a project’s migrations and their status.
   1. Migrate DB by command:
      - Windows OS: `python manage.py migrate`
            More about migrations for Django is [here](https://docs.djangoproject.com/en/4.1/topics/migrations/) 
      - MacOS:
   2. Load data from your fixture files by command: ` python manage.py loaddata <yourFixtureFileName>.json
   

### 3. Update DB content
1. Add several instances in the Data and Model tables.
2. New data engine is not working and all data that requests from DB should be pasted manually  

# Routes

* **{serverURL}/home** - Home page
* **{serverURL}/source/{pk}**  -  Source page. Specific [age of selected source. It contains list of items that are related to selected source 
* **{serverURL}/sources_list**  - main page of sources. Page that contains all sources (list view)  
* **{serverURL}/sources_table**  - main page of sources. Page that contains all sources (table view)

# TIPS

1. [FIX for "SECURITY WARNING: keep the secret key ](https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl)
2. Article: [Python Requirements.txt – How to Create and Pip Install Requirements.txt in Python3.](https://www.freecodecamp.org/news/python-requirementstxt-explained/) 
3. Single command for generating requirements.txt
`pip freeze > requirements.txt`
4. Step-by-Step Guide to Creating Python Virtual Environments ()
   * Step 1: verify python installation\
         `python –version` 
   * Step 2: install virtualenv\
      `pip install virtualenv`
   * Step 3: create a new virtual environment\
   `python -m virtualenv .venv`
   * Step 4: activate the virtual environment
      * For _Windows_ (Command Prompt or PowerShell):\
      `.venv\Scripts\activate`
       * For _Unix/Linux_ (Bash/Zsh):\
          `source venv/bin/activate`


# Django - FAQ
## Installed python modules (aka requirements.txt)
pip install django-debug-toolbar

## Typical Django project structure

project_name/\
|-- manage.py\
|-- project_name/\
|   |-- __init__.py\
|   |-- settings.py\
|   |-- urls.py\
|   |-- asgi.py\
|   -- wsgi.py\
|-- app_name/\
|   |-- __init__.py\
|   |-- admin.py\
|   |-- apps.py\
|   |-- migrations/\
|   |   -- __init__.py\
|   |-- models.py\
|   |-- views.py\
|   |-- tests.py\
|   -- templates/\
|       -- app_name/\
|           -- template_name.html\
|-- static/\
|   -- app_name/\
|       -- style.css\
|-- media/\
|-- templates/\
|   -- base.html\
|-- requirements.txt\
-- venv/\

_Explanation:_

* 'project_name/': This is the main folder for your Django project.
  * **manage.py**: Command-line utility to interact with your project.
  * **project_name/**: The inner folder with the same name as your project.
  * **__init__.py**: An empty file that tells Python that this directory should be considered a Python package.
  * **settings.py**: Configuration settings for your project.
  * **urls.py**: URL patterns for your project.
  * **asgi.py**: Configuration for ASGI (Asynchronous Server Gateway Interface).
  * **wsgi.py**: Configuration for WSGI (Web Server Gateway Interface).
* **app_name/**: This is a Django app within your project.
  * **__init__.py**: Marks the directory as a Python package.
  * **admin.py**: Configuration for the Django admin interface.
  * **apps.py**: Configuration for the app itself.
  * **migrations/**: Database migration files.
  * **models.py**: Database models.
  * **views.py**: Views and business logic.
  * **tests.py**: Unit tests.
  * **templates/**: HTML templates for the app.
* **static/**: Static files like CSS, JS, and images.
* **media/**: User-uploaded media files.
* **templates/**: Shared templates for the entire project.
* **requirements.txt**: Python dependencies for your project.
* **venv/**: Virtual environment (optional but recommended for isolation).

For custom methods, extra actions, or additional functionalities, you can create modules or packages within your app and organize them as needed. For example:

Create a **utils/** or **helpers/** package within your app to store utility functions.
Add a **services/** package to encapsulate business logic.
Use **management/** for custom management commands.