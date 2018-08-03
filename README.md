Django Game App

Created a new Django application with sqlite3 as the database
Write models using Django

created a virtual enviroment
installed dependencies using pip install and used pip freeze to save them to requirements.txt
created project 'project4game'
run 'python manage.py runserver' and then navigated to localhost:8000.  see welcome page in Django.

created my models in project4game/models.py
ran 'python manage.py makemigrations' in order to migrate the models to the database.
commited the migrantion to teh database with the below command
python manage.py migrate

created a superuser 
python manage.py createsuperuser

created some views in views.py to display in my application data
updated the urls.py in the project4game directory.

created base.html to add some styling to my views using bootstrap
created full crud functionality on one model (so far)
