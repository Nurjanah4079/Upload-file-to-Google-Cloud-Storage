#pip install --upgrade google-cloud-storage
# import library
from google.cloud import storage
import urllib.request

project_id = 'program-data-fellowship-8' 
bucket_name = 'datafellowship-8' 
destination_blob_name = 'logo_google_storage.jpg'
source_file_name = 'https://download.logo.wine/logo/Google_Storage/Google_Storage-Logo.wine.png'
storage_client = storage.Client.from_service_account_json('program-data-fellowship-8-a5ab19db710f.json')

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    file = urllib.request.Request(source_file_name, headers={'User-Agent': 'Mozilla/5.0'})   
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    name = urllib.request.urlopen(file).read()
    blob.upload_from_string(name, content_type='image/jpg')

upload_blob(bucket_name, source_file_name, destination_blob_name)

