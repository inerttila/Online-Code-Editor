from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox(), etc., depending on your browser
driver.get('https://skaitech.al/en/store/')

# Scroll down to load content, waiting for 3 seconds each time
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the new content
    time.sleep(3)
    # Check if the page height has increased
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # No new content loaded
        break
    last_height = new_height

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()  # Close the browser

product_names = []
for product in soup.select('span a[title]'):
    name = product.get_text(strip=True)  # Extract and clean the text
    product_names.append(name)

# Write the product names to a text file
with open('text.txt', 'w') as f:
    for name in product_names:
        f.write(name + '\n')

print(f"Extracted {len(product_names)} product names and saved to text.txt.")