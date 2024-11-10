
# **Mimir**

A Django-based NLP interpreter built with spaCy and PyTextRank. It processes text files by extracting specified spaCy token types. The extracted data, including tokens and their associated metadata, is persisted and used to generate csv files enabling easy export.    

<br>

- [**Table of Contents:**](#table-of-contents)
    - [**Features**](#features)
    - [**Technologies**](#technologies)
    - [**Deployment**](#deployment)
    - [**Database Design**](#database-design)
    
<br>

## Features:

**Management command**
- A utility command to trigger spaCy text processing. To run this command, add below to terminal:

    ```
    python manage.py interesting_words
    ```

 **Adaptive data folder**
- Data folder, where text files are read/processed from. Add manually, see location:

    ```
    mimir\data\text_data
    ```

<br>

## Technologies:

- **Python**    
    - [Python 3.11.0](https://www.python.org/) - Used as base language.
- **Django**
    - [Django 4.2.11](https://www.djangoproject.com/) - A Python web framework for rapid development.
- **SpaCY**
    - [spaCy 3.7.4](https://spacy.io//) - An open-source library for natural language processing in Python.
- **Poetry**
    - [Poetry 1.8.3](https://python-poetry.org/) - For dependency management and packaging in Python.
- **Database**
    - [SQlite 3.38.4](https://www.sqlite.org/index.html) - For a development database, provided by Django.


<br>

## Deployment:

### Local Deployment:

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/) to run the application.
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) to install app requirements.
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for version control.

1. Clone the Mimir repository by either downloading from here or type the following command into your terminal:
    ```
    git clone https://github.com/isntlee/Mimir
    ```
2. Navigate into Mimir:
    ```
    cd Mimir 
    ```
3. Install all the requirements and dependancies with the command:
    ```
    poetry install
    ``` 
4. Activates the virtual environment managed with Poetry: 
    ```
    poetry shell 
    ```
5. Migrate the admin models to create your database template with the terminal command:
    ```
    python manage.py migrate
    ```
6. Create your superuser to access the django admin panel and database with the following command:
    ```
    python manage.py createsuperuser
    ```
7. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
     ```
8. Once the program is running, go to localhost and add `/admin/` to the end of the url. Here log in with the initial superuser account.

9. Create an .env file at root level where you can store your sensitive information for the app. Add these details to that file:
    ```
    SECRET_KEY = "SECRET_KEY"
    DEBUG = "DEBUG"
    ```
10. Create a new and truly secret key, which will be generated in a secret_key.txt file at root level, with this command:
    ```
    python core/generate_key.py
    ```
11. Find the SECRET_KEY and DEBUG variables in the core/settings.py file. You'll find two sets of SECRET_KEY and DEBUG variables: commented out and uncommented. You should comment out the uncommented, and vice-versa.

12. Finally, set the variables in your .env file. Set SECRET_KEY to the text found in secret_key.txt, remember to add '' as it should be a string. Set DEBUG to whatever you prefer, there are no security problems with DEBUG = 'True' in development. However, do change for production. 

<br>

## Database Design:

- [SQlite](https://www.sqlite.org/index.html) - For development database, provided by Django.

### Data Models:

**User model**

The User model utilized for this project is the standard one provided by **`django.contrib.auth.models`**

\
**Word model**

| Name | Key in DB | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=250 | CharField
Sentence  | sentence  | max_length=2500 | CharField
Document  | document  | max_length=250 | CharField
Job_ID   | job_id   | max_length=250, null=True | CharField
Constraint  | constraint  | max_length=250 | CharField
Active | active | default=True, null=True | BooleanField

<br>
