import requests

# Set up the API key
api_key = "YOUR_API_KEY"

# Define the base URL for the API
base_url = "https://api.repl.it"

# Create a new repl
def create_repl(name, language):
    endpoint = f"{base_url}/v0/repls"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"name": name, "language": language}
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data

# Example: create a new Python repl
repl_name = "MyRepl"
repl_language = "python"
response_data = create_repl(repl_name, repl_language)
print("Repl created successfully!")
print("Repl ID:", response_data["id"])
print("Repl URL:", response_data["url"])
