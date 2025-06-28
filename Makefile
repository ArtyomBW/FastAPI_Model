mig:  # o'zgarishlarni yozadi
	alembic revision --autogenerate -m "Create a baseline migrations"

head: # databaseda bajaradi
	alembic upgrade head

push:
	@read -p "Commit izohini kiriting: " m; \
	git add . ; \
	git commit -m "$$m"; \
	git push

