# OpenCV
## Course project in Project for Data Science at SNU, fall of 2022

## Backend

The backend is written in Python. We use a simple Flask server, and it is deployed with Google Cloud App Engine. 
This is a serverless service that automatically scales our backend code. 
The model inference is done with our custom model that will be fetched from Google Cloud Storage.

### Running locally
You can run the backend locally with docker using either 
```
make start-backend
```
running the docker compose commands yourself. 
The app will then expose our apis on `localhost:8080`.

If you want to reload the app without rebuilding every image run
```bash
make reload-backend
```

You can also run it directly on your local machine. Make sure to use `python3.8` and 
install the requirements in `requirements.txt`. Also make sure to update 
this file whenever new requirements are added. 

### Deploying
NB! our Google Cloud Platorm account is not yet set up, so do not deploy anything yet (you can't either haha)
Deployments should also be handled in our pipeline once everything is set up.
####  Google Cloud SDK
If you want to play around with it: (should not be needed at all unless you want to learn more)
Follow install instructions [here](https://cloud.google.com/sdk/docs/install-sdk): 

#### Running the deploy
Simply run the command 
```bash
gcloud app deploy
```
while inside the `root/backend` directory.
