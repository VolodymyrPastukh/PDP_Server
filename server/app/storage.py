import os
from google.cloud import storage
import base64

_BUCKET_NAME = 'pdp_bucket_1'
_BUCKET_STORAGE = 'STANDARD'
_BUCKET_LOCATION = 'us-central1'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'/app/ga.json'

storage_client = storage.Client()
bucket = storage_client.bucket(_BUCKET_NAME)

def upload_image(image_base, image_prefix=''):
    decoded_data=base64.b64decode((image_base))
    image_prefix = hash(image_prefix)
    filename = f'{image_prefix}.jpg'
    blob = bucket.blob(filename)
    blob.upload_from_string(decoded_data, content_type='image/jpg')
    blob.make_public()

    return blob.public_url
