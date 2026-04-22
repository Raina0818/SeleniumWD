from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_open_google():
    # Set up Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Verify the title
    assert "Google" in driver.title
    print("Test passed: Google page opened successfully.")
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_open_google()