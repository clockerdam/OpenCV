from google.cloud import storage
from dotenv import dotenv_values
from model.Job import Job

config = dotenv_values(".env")

def read_job_keywords(job_title: str) -> str:
    storage_client = storage.Client()
    bucket_name = config["STORAGE_BUCKET"]
    bucket = storage_client.bucket(bucket_name)
    
    file_name = f"{job_title}.csv"
    
    exists = storage.Blob(bucket=bucket, name=file_name).exists(storage_client)
    contents = ""

    if exists:
        blob = bucket.blob(file_name)
        
       
        contents = blob.download_as_string().decode('utf8')
        
    return contents

def write_job_keywords(job: Job): 
    """Writes the keyword list of a job title to the GS bucket"""
    storage_client = storage.Client()
    bucket_name = "p4ds-group2-job-title-kw-bucket"
    bucket = storage_client.bucket(bucket_name)
    
    file_name = f"{job.name}.csv"
    blob = bucket.blob(file_name)
    
    csv_string = "\n".join([f"{k},{v}" for k, v in job.keywords.items()])
    
    blob.upload_from_string(csv_string)
    
    
