#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import os 

REPLIT_API_TOKEN = os.environ['REPLIT_API_TOKEN']
BASE_URL = "https://api.repl.it"

# Create a new repl
def create_repl(name, language):
    endpoint = f"{BASE_URL}/v0/repls"
    headers = {"Authorization": f"Bearer {REPLIT_API_TOKEN}", "Content-Type": "application/json"}
    data = {"name": name, "language": language}
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data

if __name__ == "__main__":
    repl_name = input("[+] Enter the name of repl you want to create:\n[=] ")
    repl_language = "python"
    response_data = create_repl(repl_name, repl_language)
    print("Repl created successfully!")
    print("Repl ID:", response_data["id"])
    print("Repl URL:", response_data["url"])
