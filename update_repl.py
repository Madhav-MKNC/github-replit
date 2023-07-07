import requests

# Set up the API key and repl ID
api_key = "YOUR_API_KEY"
repl_id = "YOUR_REPL_ID"

# Define the base URL for the API
base_url = "https://api.repl.it"

# Update the repl
def update_repl(repl_id, new_code):
    endpoint = f"{base_url}/v0/repls/{repl_id}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"files": [{"name": "main.py", "content": new_code}]}
    response = requests.put(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data

# Example: update the code in the repl
new_code = """
print('Updated code!')
"""
response_data = update_repl(repl_id, new_code)
print("Repl updated successfully!")
print("Repl ID:", response_data["id"])
print("Repl URL:", response_data["url"])
