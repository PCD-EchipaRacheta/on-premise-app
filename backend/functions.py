from google.cloud import storage
from google.cloud import secretmanager
import os

def upload_to_gcs(source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    try:
        # Check if credentials are set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError(
                "The environment variable 'GOOGLE_APPLICATION_CREDENTIALS' is not set. "
                "Please set it to the path of your Google Cloud credentials JSON file."
            )
        
        client = storage.Client()
        bucket = client.bucket("weather-data1")
        blob = bucket.blob(destination_blob_name)
        
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# upload_to_gcs("local_file.txt", "uploaded_file.txt")

def download_from_gcs(source_blob_name, destination_file_name):
    """Downloads a file from Google Cloud Storage."""
    try:
        # Check if credentials are set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError(
                "The environment variable 'GOOGLE_APPLICATION_CREDENTIALS' is not set. "
                "Please set it to the path of your Google Cloud credentials JSON file."
            )
        
        client = storage.Client()
        bucket = client.bucket("weather-data1")
        blob = bucket.blob(source_blob_name)
        
        blob.download_to_filename(destination_file_name)
        print(f"File {source_blob_name} downloaded to {destination_file_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# download_from_gcs("uploaded_file.txt", "downloaded_file.txt")

def delete_gcs_file(blob_name):
    """Deletes a file from GCS."""
    try:
        # Check if credentials are set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError(
                "The environment variable 'GOOGLE_APPLICATION_CREDENTIALS' is not set. "
                "Please set it to the path of your Google Cloud credentials JSON file."
            )
        
        client = storage.Client()
        bucket = client.bucket("weather-data1")
        blob = bucket.blob(blob_name)
        blob.delete()
        print(f"File {blob_name} deleted from weather-data1.")
    except Exception as e:
        print(f"An error occurred: {e}")

# delete_gcs_file("uploaded_file.txt")

def list_gcs_files():
    """Lists all files in a GCS bucket."""
    try:
        # Check if credentials are set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError(
                "The environment variable 'GOOGLE_APPLICATION_CREDENTIALS' is not set. "
                "Please set it to the path of your Google Cloud credentials JSON file."
            )
        
        client = storage.Client()
        bucket = client.bucket("weather-data1")
        blobs = bucket.list_blobs()
        
        print("Files in bucket:")
        for blob in blobs:
            print(blob.name)
    except Exception as e:
        print(f"An error occurred: {e}")

# list_gcs_files()





def access_secret_weatherAPIKey():
    """Access a secret from Google Cloud Secret Manager."""
    try:
        # Check if credentials are set
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError(
                "The environment variable 'GOOGLE_APPLICATION_CREDENTIALS' is not set. "
                "Please set it to the path of your Google Cloud credentials JSON file."
            )
        
        client = secretmanager.SecretManagerServiceClient()
        project_id = "41335490407"
        secret_id = "weatherAPI-key"
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception as e:
        print(f"An error occurred: {e}")

# print(f"Retrieved API Key: {access_secret_weatherAPIKey()}")