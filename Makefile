mig:  # o'zgarishlarni yozadi
	alembic revision --autogenerate -m "Create a baseline migrations"

head: # databaseda bajaradi
	alembic upgrade head


