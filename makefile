start-backend: 
	@echo "Starting the entire backend with database"
	docker-compose up -d --build

reload-backend: 
	@echo "reloading the backend with docker compose (no db reload)"
	docker compose up -d --build backend

stop-backend:
	@echo "Stopping the entire backend with database"
	docker compose down

# Only for use in the pipeline
create-env: 
	@echo "Creating .env file"
	touch root/backend/.env
	printenv > root/backend/.env

build-and-deploy-image:
	@echo "building and deploying docker image"
	docker build -t asia.gcr.io/p4ds-team-2/p4ds-backend root/backend
	docker push asia.gcr.io/p4ds-team-2/p4ds-backend


