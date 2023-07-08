#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import pyrepl
import os

REPLIT_API_TOKEN = os.environ['REPLIT_API_TOKEN']
REPL_ID = "" # pyrepl.get_json()
BASE_URL = "https://api.repl.it"

# Update the repl
def update_repl(repl_id, file_name, new_code):
    endpoint = f"{BASE_URL}/v0/repls/{repl_id}"
    headers = {"Authorization": f"Bearer {REPLIT_API_TOKEN}", "Content-Type": "application/json"}
    data = {"files": [{"name": file_name, "content": new_code}]}
    response = requests.put(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data


if __name__ == "__main__":
    new_code = 'print("IT WORKS")'
    response_data = update_repl(REPL_ID, test.py, new_code)
    print("Repl updated successfully!")
    print("Repl ID:", response_data["id"])
    print("Repl URL:", response_data["url"])
