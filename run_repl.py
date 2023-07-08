#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import os
import pyrepl

REPLIT_API_TOKEN = os.environ['REPLIT_API_TOKEN']
REPL_ID = "" # pyrepl.get_json()
BASE_URL = "https://api.repl.it"

# Run the main file in the repl
def run_main_file(repl_id):
    endpoint = f"{BASE_URL}/v0/repls/{repl_id}/run"
    headers = {"Authorization": f"Bearer {REPLIT_API_TOKEN}", "Content-Type": "application/json"}
    data = {"runMain": True}
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data

if __name__ == "__main__":
    response_data = run_main_file(repl_id)
    print("Repl execution started!")
    print("Session ID:", response_data["id"])
    print("Console output:")
    print(response_data["consoleOutput"])
