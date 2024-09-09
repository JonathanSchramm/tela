from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure options if needed
chrome_options = Options()
# Add any necessary options here, e.g., chrome_options.add_argument('--headless')

# Start the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the desired URL
driver.get("https://www.linkedin.com/feed/")

# Do not call driver.quit() to keep the browser open
# You will need to manually close the browser window when done
