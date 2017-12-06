This small, single-page application was developed as a hiring project for the
company BriteCore. BriteCore produces an enterprise-level insurance processing
suite. The purpose of this project was to design a table structure within a 
relational database that would allow a user of the application to define their 
own types of risk. The project required a front end that would display a form
for the risk type containing it's designated fields. Each input field must be
of the appropriate type (text, number, date, or select), designated in the 
database. Submit functionality was not required.

My solution uses the Django framework, so to run it you must have
Django installed. Installation instructions are available at
https://docs.djangoproject.com/en/1.11/intro/install/.

Here are the steps to run the application once you have the source folder
downloaded:

1) In the command line, go to the root folder for the application.
2) Start the development server by running the command:
   python manage.py runserver
3) In your web browser, go to the address http://127.0.0.1:8000/britecoreapp/risktype/Automobile/

Here is a rundown of the source code:

- Data layer designed at britecoreproject/britecoreapp/models.py
- Entity relationship diagram located at britecoreproject/BriteCoreERD.pdf
- Migration which seeds the database located at britecoreproject/britecoreapp/migrations/0001_initial.py
- GET request handler defined at britecoreproject/britecoreapp/views.py
- Front end HTML template located at britecoreproject/britecoreapp/templates/risktype/index.html
