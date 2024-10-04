weka:
	git add .
	git commit -m "LMS_API"
	git push


db:
	python manage.py makemigrations
	python manage.py migrate

all:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver 

delete:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm db.sqlite3

run:
	python manage.py runserver