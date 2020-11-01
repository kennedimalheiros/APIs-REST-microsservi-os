runserver:
	docker-compose run --rm --name server web python manage.py runserver 0:8001

migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

superuser:
	docker-compose run web python manage.py createsuperuser

shell:
	docker-compose run web python manage.py shell

populate:
	docker-compose run web python manage.py populate_db

build:
	docker-compose build