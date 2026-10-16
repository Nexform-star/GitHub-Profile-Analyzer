# GitHub Profile Analyzer

A beginner-friendly Python CLI tool that analyzes public GitHub profiles and repositories using the GitHub REST API.

This project is built to improve my Python skills and understand how to work with APIs, process JSON data, calculate statistics, and manage paginated requests.

## Features

### GitHub Profile Analysis

Retrieve public information about a GitHub account, including:

- Username
- Display name
- Biography
- Account creation date
- Number of public repositories
- Followers and following

### Repository Analysis

Retrieve and analyze a user's public repositories, including:

- Repository name
- Description
- Primary programming language
- Stars
- Forks

Missing descriptions and programming languages are handled with fallback values to keep the output readable.

### Repository Statistics

Calculate statistics from the repositories retrieved through the GitHub API:

- Total number of repositories analyzed
- Total stars across the repositories
- Total forks across the repositories
- Most-starred repository

### Pagination

The tool retrieves repositories in pages of up to 100 items. It continues requesting subsequent pages until no more repositories are returned.

This allows the analyzer to process accounts with more than 100 public repositories.

## Technologies

- Python
- Requests
- GitHub REST API
- JSON
- Git and GitHub

## Requirements

- Python 3.10 or later
- An internet connection
- The `requests` library

## Installation

Clone the repository:

```bash
git clone https://github.com/Nexform-star/GitHub-Profile-Analyzer.git
```

Move into the project directory:

```bash
cd GitHub-Profile-Analyzer
```

Install the required dependency:

```bash
python -m pip install requests
```

## Usage

Run the main Python script:

```bash
python main.py
```

Follow the command-line menu and select the analysis you want to perform. Enter the GitHub username when prompted.

The tool retrieves publicly available information from the GitHub REST API and displays the results in the terminal.

## Development History

The project has been developed incrementally, with each step introducing a new concept or improvement.

### Stage 1 — Initial CLI and API integration

- Created the command-line interface.
- Added requests to the GitHub REST API.
- Implemented the first profile and repository analysis features.

### Stage 2 — Profile information and repository statistics

- Added public profile fields such as the username, biography, followers, following, and account creation date.
- Added repository details such as names, descriptions, languages, stars, and forks.
- Implemented calculations for total stars, total forks, and the most-starred repository.

### Stage 3 — Pagination

- Added support for retrieving repositories across multiple API pages.
- Configured requests to retrieve up to 100 repositories per page.
- Added a counter for the total number of repositories processed.

### Stage 4 — Request parameter improvements

- Moved pagination settings into the request's `params` dictionary.
- Kept the page number and page size as separate parameters.
- Improved the structure of API requests.

These stages describe the development progress of the project. They do not necessarily correspond to published Git tags or formal releases.

## Project Status

The project is under development. Its current focus is on learning Python, improving API handling, and building reliable repository statistics.

Future improvements may include more detailed statistics, better error handling, and report exports.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
