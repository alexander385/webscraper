# Web Scraper for Google Search Results

## Overview
This project is a web scraper developed as part of an application for a start-up. The goal of this scraper is to automate the process of searching for products on Google based on a user-defined search phrase and extracting the title and URL of the first search result.

## Features
- Accepts a user-provided search phrase.
- Automatically accepts Google cookies.
- Searches for the given phrase on Google.
- Extracts the title and URL of the first search result.
- Outputs the extracted information to the console.

## Technologies Used
- Python
- Selenium
- Chrome WebDriver
- WebDriver Manager
- Requests

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Google Chrome](https://www.google.com/chrome/)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/webscraper-startup.git
   cd webscraper-startup
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   **Note:** The `requirements.txt` should contain:
   ```
   selenium
   webdriver-manager
   requests
   ```

## Usage
1. Run the script using the following command:
   ```bash
   python scraper.py
   ```
2. Enter your desired search phrase when prompted.
3. The script will:
   - Open Google
   - Accept cookies
   - Perform a search for the given input
   - Extract and print the first result's title and URL.

## Code Explanation
The script performs the following steps:
1. Takes user input for a search query.
2. Opens Google and accepts cookies.
3. Searches for the provided query.
4. Extracts the first search result link and navigates to it.
5. Prints the page title and URL.
6. Handles exceptions such as element not found or timeout issues.

## Error Handling
The script includes basic error handling to catch exceptions such as:
- `NoSuchElementException` if an element is not found.
- `TimeoutError` if the page takes too long to load.

## Future Improvements
Some possible improvements for future versions include:
- Scraping multiple results instead of just the first one.
- Storing results in a database or CSV file.
- Adding headless browsing for better performance.
- Implementing proxy support for anonymity.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.


