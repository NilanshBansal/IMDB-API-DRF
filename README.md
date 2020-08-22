# IMDB APP
 
### Setup on Local machine

- virtualenv venv --python=python3
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### You can use it at https://lms-nilansh.herokuapp.com/

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

### Application Routes

1. /user/create/
2. /admin/create/
3. /listmovies/
4. /movies/
5. /search/
6. /putordelete/<id>
