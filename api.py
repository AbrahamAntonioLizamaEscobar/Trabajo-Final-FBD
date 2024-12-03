import requests

API_URL = "API_BASE_URL"

# Login
def login_user(username, password):
    try:
        response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

# Fetch Data
def fetch_data(endpoint):
    try:
        response = requests.get(f"{API_URL}/{endpoint}")
        return response.json()
    except Exception as e:
        return []

# Post Data
def post_data(endpoint, data):
    try:
        response = requests.post(f"{API_URL}/{endpoint}", json=data)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}
