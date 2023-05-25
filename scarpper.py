import requests
from bs4 import BeautifulSoup

# Specify your Instagram username
username = "your_username"

# Create the URL for your following page
url = f"https://www.instagram.com/{username}/following/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the user profiles
user_profiles = soup.find_all("div", {"class": "wFPL8"})

# Iterate over each user profile
for user_profile in user_profiles:
    # Extract the username
    username = user_profile.find("a").get("href")[1:-1]
    
    # Extract the bio (if available)
    bio = user_profile.find("span").text.strip()
    
    # Print the username and bio
    print("Username:", username)
    print("Bio:", bio)
    print()
