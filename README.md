# Instagram Automation Script 📸

This project is an Instagram automation script that logs into an Instagram account, navigates to a specified user's followers list, and interacts with the followers' action buttons. The script is built using Python and Selenium.

## Features
- 🌐 Loads an Instagram profile page.
- 🔐 Logs in using Instagram credentials from environment variables.
- 🍪 Accepts cookies to proceed with the script.
- 📃 Retrieves and interacts with the followers list.

## Prerequisites
- Python
- Chrome WebDriver
- Instagram account credentials stored in environment variables (`NAME` and `PASSWORD`).

## Functional Requirements
1. **Load Instagram Page**
   - Loads the specified Instagram profile page.

2. **Login to Instagram**
   - Logs into Instagram using the provided credentials.

3. **Accept Cookies**
   - Clicks the button to accept cookies.

4. **Retrieve Followers List**
   - Navigates to the followers list of the specified profile and interacts with it.

## Setup
1. **Clone the repository**
   ```bash```
    ```git clone https://github.com/yourusername/instagram-automation-script.git```
    ```cd instagram-automation-script ```
   
   2. **Install dependencies** ```bash pip install selenium ```
   3. **Download Chrome WebDriver** - Download the appropriate version of Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your project directory.
   4. **Set environment variables** - Create a `.env` file in the project directory and add the following variables: ``` NAME=<your_instagram_username>
PASSWORD=<your_instagram_password> ```
     
## Running the Script 
1. **Run the script** ```bash python main.py ```

## Files 
- `main.py`: The main script that performs the Instagram automation.
- `.env`: Environment variables file (not included in the repository, needs to be created).

## Important Notes 
- Ensure your `.env` file is not included in version control to keep your credentials safe. - Replace placeholder values in the `.env` file with your actual Instagram credentials. ## Common Issues - If you encounter an error related to the Instagram credentials, ensure that your `.env` file is correctly formatted and the `NAME` and `PASSWORD` variables are set.
