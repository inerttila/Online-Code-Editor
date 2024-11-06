from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox(), etc., depending on your browser
driver.get('https://3dskai.com/en/shop/')

# Initialize an empty list to store product names
product_names = []

# Loop through pagination pages
while True:
    # Wait for the page to load
    time.sleep(3)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for product in soup.select('span a[title]'):
        name = product.get_text(strip=True)  # Extract and clean the text
        product_names.append(name)

    # Try to find the "Next" button and click it
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.next')  # Update this selector to match the "Next" button
        next_button.click()
    except NoSuchElementException:
        # Break the loop if there is no "Next" button (end of pagination)
        break

# Close the browser
driver.quit()

# Write the product names to a text file
with open('text.txt', 'w') as f:
    for name in product_names:
        f.write(name + '\n')

print(f"Extracted {len(product_names)} product names and saved to text.txt.")
