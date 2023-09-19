import requests

# Create a session
session = requests.Session()

url = "http://127.0.0.1:8000"
response = session.get(url)
csrf_token = response.cookies['csrftoken']
print(response)

# Step 2: Log in with the obtained CSRF token
url = "http://127.0.0.1:8000/login"
payload = {
    'email': 'user1@example.com',
    'password': 'oXhqNLvLvF9gGfP3JYWg',
    'csrfmiddlewaretoken': csrf_token,
}
response = session.post(url, data=payload)
print(response.status_code)

# Step 3: Make a request to the inbox page
url = "http://127.0.0.1:8000/emails/sent"
response = session.get(url)
print(response.status_code)

# Close the session when done (optional)
session.close()
