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
1. /user/create/
2. /admin/create/
3. /listmovies/
4. /movies/
5. /search/
6. /putordelete/<id>

| Method        | Route           | Parameters  | Description  |
| ------------- |:-------------:|:-------------:| ----- |
| POST      | /user/create | username, password | Creates a user |
| POST      | /admin/create | username, password | Creates an admin |
| GET       | /listmovies/  | NA | Lists all movies present in the db. Auth required (User/admin) |
| POST      | /movies/ | Raw JSON from json file shared | Populates the db with movies. Auth required (Admin)|
| POST      | /search/ | name,genre,director | Searches the db with the relevant parameters on movie name,genre or director. All param optional. If no param added, returns all movies.  Auth required (User/admin)|
| PUT      | /putordelete/<id> | Updated Raw Movie json | Updates the movie with the id from db. Auth required (Admin)|
| DELETE      | /putordelete/<id> | NA | Deletes the movie with the id from db. Auth required (Admin)|


Note: Wherever Authentication is required use Basic Auth with username and password for User/Admin respectively