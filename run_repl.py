import requests

# Set up the API key and repl ID
api_key = "YOUR_API_KEY"
repl_id = "YOUR_REPL_ID"

# Define the base URL for the API
base_url = "https://api.repl.it"

# Run the main file in the repl
def run_main_file(repl_id):
    endpoint = f"{base_url}/v0/repls/{repl_id}/run"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"runMain": True}
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data

# Example: run the main file in the repl
response_data = run_main_file(repl_id)
print("Repl execution started!")
print("Session ID:", response_data["id"])
print("Console output:")
print(response_data["consoleOutput"])
