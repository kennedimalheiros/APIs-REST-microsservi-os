runserver:
	docker-compose run --rm --name client web python manage.py runserver 0:8000

migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

superuser:
	docker-compose run web python manage.py createsuperuser

shell:
	docker-compose run web python manage.py shell

build:
	docker-compose build