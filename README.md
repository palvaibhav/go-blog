
# Go-Blog

A blogging website where users can register/login to create new posts, update and delete posts.

  
## Features

1. Registered users can add comments.

2. Registered users can upvote or downvote a post.

3. Use API endpoints to fetch data from the app.

  

# Steps to install

  

## 1.Cloning the Repository

Clone the repository and navigate to the go-blog folder.

```
	git clone https://github.com/palvaibhav/go-blog.git
	cd go-blog
```

## 2. Creating a virtual environment

Create virtual Environment where you will install all the required packages.

```
	virtualenv venv
	source venv/bin/activate
```

  

## 3. Setting up Database and Connecting to PostgresSQL

1. Install PostgresSQL to local machine

```
	sudo apt-get install postgresql postgresql-contrib
	sudo -u postgres createuser --superuser <name_of_user>
```

2. Create Database

```
	sudo -u <name_of_user> createdb <name_of_db>
	psql -U <name_of_user>  -d <name_of_db>
```

3. In config.py add the following line:-
```
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```
4. In ~/.bashrc add the following line:-
```
	export DATABASE_URL="postgresql:///<name_of_db>"
```
5. Create file manage.py

6. Install required packages from requirements.txt file

```
	pip install -r requirements.txt
```

7. Create migrations folder

```
	python manage.py db init
	python manage.py db migrate
	python manage.py db upgrade
```
8. Run the server and open the browser and type localhost:5000

```
	python manage.py runserver
```
