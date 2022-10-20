start-backend: 
	@echo "Starting the entire backend with database"
	docker compose up -d --build

reload-backend: 
	@echo "reloading the backend with docker compose (no db reload)"
	docker compose up -d --build backend
