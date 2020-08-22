# IMDB APP
 
### Setup on Local machine

- virtualenv venv --python=python3
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### Hosted at https://imdb-nilansh.herokuapp.com/

### Superuser details
Username: nilansh  
Email: bansalnilansh@gmail.com  
Password: Hello@123  

### Admin Account
Username: testadmin  
Password: password  

### User Account
Username: testuser  
Password: password  
 
### WorkFlow:

1. There are 2 levels of users - Admin and User
2. Admin can add, remove and edit movies.
3. User can just view the movies. 

### You can access the postman collection at https://www.getpostman.com/collections/cbe2b10a69ebd15f34a4

### Application Routes

| Method        | Route           | Parameters  | Auth  |Description  |
| ------------- |:-------------:|:-------------:| :-----: | ----- |
| POST      | /user/create | username, password | NA | Creates a user |
| POST      | /admin/create | username, password |  NA | Creates an admin |
| GET       | /listmovies/  | NA | Admin/User | Lists all movies present in the db |
| POST      | /movies/ | Raw JSON from json file shared | Admin | Populates the db with movies|
| POST      | /search/ | name,genre,director | Admin/User | Searches the db with the relevant parameters on movie name,genre or director. All param optional. If no param added, returns all movies|
| PUT      | /putordelete/<id> | Updated Raw Movie json | Admin | Updates the movie with the id from db|
| DELETE      | /putordelete/<id> | NA | Admin | Deletes the movie with the id from db|


**Note:** Wherever Authentication is required use Basic Auth with username and password for User/Admin respectively