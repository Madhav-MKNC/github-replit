<h1>[ UNDER DEVELOPEMENT ]</h1>

# GitHub-Replit Sync
Allows you to host a program on Replit and regularly sync it with your GitHub repository. Just a few commands and host your github repository on repl.it

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- Python 3.6 or above installed on your machine.
- An account on Replit to host your program.
- API tokens for Replit and GitHub (instructions on how to obtain them are provided below).

# Getting Started

To get started with this script, follow these steps:

### Clone the repository to your local machine using the following command:
   ```(bash)
   git clone <repository-url>
   ```

### Install the required dependencies by running the following command:
   ```(bash)
   pip install -r requirements.txt
   ```

### Obtain the required API tokens:

- For Replit: Go to your Replit account settings and generate a new API token.
- For GitHub: Create a personal access token on GitHub with the necessary repository permissions.

### Update the configuration in the `.env` file:

- Set the `REPLIT_API_TOKEN` variable to your Replit API token.
- Set the `GITHUB_API_TOKEN` variable to your GitHub API token.
- Modify any other settings according to your requirements.

### Run the script using the following command:
   ```(bash)
   python main.py
   ```

The script will start syncing your Replit project with the GitHub repository.

## Configuration

The `.env` file contains the configuration options for the script. You can modify the following settings:

- `REPLIT_API_TOKEN`: The API token for your Replit account.
- `GITHUB_API_TOKEN`: The API token for your GitHub account.
- `REPLIT_PROJECT_ID`: The ID of your Replit project (can be found in the Replit project URL).
- `GITHUB_REPO_OWNER`: The owner/username of the GitHub repository.
- `GITHUB_REPO_NAME`: The name of the GitHub repository.

## Contributing

If you find any issues, have suggestions, or would like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE).


