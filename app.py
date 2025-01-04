import firebase_admin
from firebase_admin import credentials, firestore

# Provide the Firebase credentials directly as a dictionary
cred_dict = {
    "type": "service_account",
    "project_id": "isa2025-f3173",
    "private_key_id": "33dad91dae2b4c361417c87d4bb85f1a2dab47e4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCcgcS2OvUAVb/c\nWstWE5eiJzSoZPsjKKaviQZWmGSND+sC+yqqlumQsvM0P8tCQ5CDFwMH89KzuVYq\nzt4tYh1GS+R55EtAbSBk7Zjlb/bDqAuLNAXvfCb0rJ16WrXMkzNSe6zSYfa2dYkt\njcmGTTximrjIr07w7KkgRUmAFCuQIYmar4MyWq3+rUvR0kx7L5CnJk5VKZteVRMk\ngCMidbzd8M9j4sUU46knkSEdogCPb5yQ0YvJ7+GXjIF0ubcpEEZw7B7AThj5l9S+\n1x8gExExSc3gmRmBqKkdGGzvFvyKTvu/i9hN0g+U0eNI12XEkpXA0PlsX9tb2j1d\npjp6e20bAgMBAAECggEAQm4ceoMM4k8DaHtLaqZXSvccNUvjgzlqgwCE5bW6nFuA\n09ubcRwsWIR0kZ1wX5iBGvtmCHaYXTvSVMpI6PeH2II3IPvjax3GzcBCEUUUd1j5\nSWVUDaJjgKBSGZCuMP7cHmsrYIM/bpP2HZVc0DoxYuMsgtZSihXR9cYjHA+zq/G9\n1MqihMxlOswJZk3k3y1a0JFuvFkun9nMn42M0alWP8GE9QAbC/oBt4HnzX/bi4oh\nN8Nb1H2extAwlu4qCQVoEJ6zD4XdnTqniwkO/barAeysSVBisIfwdnPzRTeeXskd\noaVauhCff/ZkTNcY4M6uR6/pSQqWkmRQ3cMdFGy50QKBgQDZDUQh0mHw4SCxamjf\n3VsD4mVTIXZB4GEqYgb2GIPmBCD5mFBNHEnjJV1ctPqzBGQKhUQzHjmHqj/65ysH\nRNzeM8n5e/4O3D787dsZqpgTMIsPe8GZYhuGcb7g0jbzFF8sK/zXDvEvd+lNNy9E\n2J+r31ASMYME++pf4jJ5zLn8MQKBgQC4lz5plZ2jukVpqswCEerbjgbg7guIDIKT\nlFxlLcdzqWlh75UQOzg0A74Yy4zlGwy0ZU1YKCKaERbODtPLzngF0/cqqYo7fwcy\nkYLz/6VT7KPLviUC6QFAl+aAJJjr1BPMn94XNE9ybGmx7a3frwHTdGumSATu4dFT\n6IPkK0xHCwKBgQCUC41mOFZfc17WREtGLnhu/NO50QAVTNNZkkVHRE9q63QGapKT\nFfF7wjedDUBWLG+EEYQEDeCVnVVIcLaTna+8y7w+tAkE38sCv8YLCqXxqNGg/Pt/\nAEDgAeN8+0VJpaKIwXQSx/lQNEzoQvS107+M/qNh1W2VT7J8Ng/RrgdJcQKBgHD/\nrSZHf7v10H4yHzb5LvN+izlwn8CGH/0l6jXKA3oLcEaSuoa4Kdy1mc5l9PdfSrS3\n+tQHpb74zSQRMZhm6VRwALOuG7/2MDrFlwu1KMkqaM7VtKSGbMzU8DbrsG1VY1V1\nXCiKTkQ2l7FjVXhEEvMWJrwhBFwUAufBw9OOqeAnAoGBANddvmIT/oHng7fBLitI\nRIbnu99LgPqguW6hL7RKv9FephdbguwtYY7egHrEUayeG7Rzn/nEaet4tHVCRERG\nmRg5UTPiu3rWEoiChtX0aVRSWfp7fo0rnlUk6veI83DaE8xb23XnrnIE4iDRm/2p\n/uT11l6yCDy8HY/V/4x1cqyU\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-5zx9w@isa2025-f3173.iam.gserviceaccount.com",
    "client_id": "106456162339754757984",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5zx9w%40isa2025-f3173.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin SDK with the provided credentials
try:
    # Convert the dictionary to credentials and initialize Firebase
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
    print("Firebase Admin SDK initialized successfully.")
except Exception as e:
    print(f"Error initializing Firebase: {e}")

# Create a Firestore client
db = firestore.client()

# Example function to save data to Firestore
def save_data(collection_name, data):
    try:
        # Access the collection and save data
        doc_ref = db.collection(collection_name).add(data)
        print(f"Data saved successfully: {doc_ref.id}")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

# Example usage
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
save_data('users', data)
