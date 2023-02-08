# news

DJANGO web app for managing parsed articles from different sources.

##Django installation

Windows

`pip install django`

Mac

`python -m pip install Django`

## Project launch process
###1. Install Django
###2. Migrate DB

<br> &nbsp;&nbsp; *Migrations* are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.
<br> &nbsp;&nbsp; *The Commands*
There are several commands which you will use to interact with migrations and Django’s handling of database schema:
<br> - _**migrate**_, which is responsible for applying and unapplying migrations.
<br> - **_makemigrations_**, which is responsible for creating new migrations based on the changes you have made to your models.
sqlmigrate, which displays the SQL statements for a migration.
<br> - **_showmigrations_**, which lists a project’s migrations and their status.

   1. migrate DB by command:
      - windows OS: `python manage.py migrate`
      - MacOS:
   2. Load data from your fixture files by command: ` python manage.py loaddata <yourFixtureFileName>.json
   

###3. Update DB content
Add several instances in the Datas and Model tables.
Npw data engine is not working and all data that requests from DB should be pasted manually  

# Routes

* **{serverURL}/home** - Home page
* **{serverURL}/source/{pk}**  -  Sorce page. Specific [age of selected source. It contains list of items that are related to selected source 
* **{serverURL}/sources_list**  - main page of sources. Page that contains all sources (list view)  
* **{serverURL}/sources_table**  - main page of sources. Page that contains all sources (table view)

#TIPS

- [FIX for "SECURITY WARNING: keep the secret key ](https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl)
