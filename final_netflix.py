from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome()

    # Test case 1: Maximize the browser window (optional)
    try:
        driver.maximize_window()
        print("Test case 1: Window maximized successfully.")
    except Exception as e:
        print(f"An error occurred in test case 1: {str(e)}")

    # Test case 2: Directing  to Netflix  page
    try:
        driver.get("https://www.netflix.com/")
        print("Test case 2: Navigated to netflix successfully.")
    except Exception as e:
        print(f"An error occurred in test case 2: {str(e)}")

    # Test case 3: Verify Netflix Login Page Loads Correctly
    try:
        driver.get("https://www.netflix.com/login")
        print("Test case 3: Navigated to Netflix Login successfully.")
    except Exception as e:
        print(f"An error occurred in test case 3: {str(e)}")

    # Test case 4: Invalid Login Credential
    try:
        driver.get("https://www.netflix.com/login")

        username = driver.find_element(By.NAME, "userLoginId")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("yashaswinigowda57@gmail.com")
        password.send_keys("yashu@123")
        password.send_keys(Keys.RETURN)
        time.sleep(4)
        print("Test case 4: Invalid username or password.")
    except Exception as e:
        print(f"An error occurred in test case 4: {str(e)}")

    # Test case 5:  login with empty credentials
    try:
        driver.get("https://www.netflix.com/login")

        username = driver.find_element(By.NAME, "userLoginId")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("raviyashaswini37@gmail.com")
        password.send_keys("")
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        print("Test case 5: enter password.")
    except Exception as e:
        print(f"An error occurred in test case 5: {str(e)}")

    # Test case 6:  successful login with valid credentials
    try:
        driver.get("https://www.netflix.com/login")

        username = driver.find_element(By.NAME, "userLoginId")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("raviyashaswini37@gmail.com")
        password.send_keys("yashaswini@37")
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Test case 6: login successful.")
    except Exception as e:
        print(f"An error occurred in test case 6: {str(e)}")

    # Test case 7: Scroll the page (example: scrolling down)
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 30  # Adjust scroll speed as needed
        for i in range(0, total_height, scroll_speed):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1)  # Adjust sleep time if needed for smoothness
        print("Test case 7: Test case for scrolling down: Scrolled the page up successfully.")
    except Exception as e:
        print(f"An error occurred in test case 7: {str(e)}")

    # Test case 8: Scroll the page (example: scrolling up)
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 30  # Adjust scroll speed as needed
        for i in range(total_height, 0, -scroll_speed):  # Scroll up from bottom to top
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1)  # Adjust sleep time if needed for smoothness
        print("Test case 8:Test case for scrolling up: Scrolled the page up successfully.")
    except Exception as e:
        print(f"An error occurred in test case for scrolling up: {str(e)}")

    # Test case 9: Clicked on PROFILE MENU
    try:
        profile_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/a'))
        )
        profile_menu.click()

        time.sleep(2)
        print("Test case 9: Clicked on profile menu.")
    except Exception as e:
        print(f"An error occurred in test case 9: {str(e)}")

    # Test case 10: Clicked on NOTIFICATION
    try:
        notification = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[2]'))
        )
        notification.click()
        time.sleep(2)
        print("Test case 10: Clicked on notification.")
    except Exception as e:
        print(f"An error occurred in test case 10: {str(e)}")

    # Test case 11: Clicked on TRAILER
    try:
        trailer = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main-view"]/div/div[1]/div/div/div/div/div/div[2]/div/div/div[3]/a'))
        )
        trailer.click()
        time.sleep(15)
        print("Test case 11: Clicked on trailer.")
    except Exception as e:
        print(f"An error occurred in test case 11: {str(e)}")

    # Test case 12: Backward navigation example (going back)
    try:
        for _ in range(1):
            driver.back()
            time.sleep(2)  # Wait for the page to load
            print("Test case 12: Navigated backward successfully.")
    except Exception as e:
        print(f"An error occurred in test case 12: {str(e)}")

    # Test case 13: Clicked on MORE INFO
    try:
        trailer = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main-view"]/div/div[1]/div/div/div/div/div/div[2]/div/div/div[3]/button'))
        )
        trailer.click()
        time.sleep(6)
        print("Test case 13: Clicked on More Info.")
    except Exception as e:
        print(f"An error occurred in test case 13: {str(e)}")

    # Test case 14: Clicked on like
    try:
        Like = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div[2]'))
        )
        Like.click()
        Like.click()
        time.sleep(4)
        print("Test case 14: Clicked on Like.")
    except Exception as e:
        print(f"An error occurred in test case 14: {str(e)}")

    # Test case 15: Backward navigation example (going back)
    try:
        for _ in range(1):
            driver.back()
            time.sleep(2)  # Wait for the page to load
            print("Test case 15: Navigated backward successfully.")
    except Exception as e:
        print(f"An error occurred in test case 15: {str(e)}")

    # Test case 16: Clicked on Movies
    try:
        AddMylist = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/ul/li[4]'))
        )
        AddMylist.click()
        time.sleep(6)
        print("Test case 16: Clicked on Movies.")
    except Exception as e:
        print(f"An error occurred in test case 16: {str(e)}")

    # Test case 17: Clicked on MOVIE TRAILER
    try:
        MovieTrailer = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main-view"]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/div[3]/a[1]'))
        )
        MovieTrailer.click()
        time.sleep(15)
        print("Test case 17: Clicked on trailer.")
    except Exception as e:
        print(f"An error occurred in test case 17: {str(e)}")

    # Test case 18: Backward navigation example (going back)
    try:
        for _ in range(1):
            driver.back()
            time.sleep(2)  # Wait for the page to load
            print("Test case 18: Navigated backward successfully.")
    except Exception as e:
        print(f"An error occurred in test case 18: {str(e)}")

    # Test case 19: Directed to My List
    try:
        Mylist = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/ul/li[6]'))
        )
        Mylist.click()
        time.sleep(6)
        print("Test case 19: Directed to mylist.")
    except Exception as e:
        print(f"An error occurred in test case 19: {str(e)}")

    # Test case 20: Directed to TV Shows
    try:
        Language = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/ul/li[3]/a'))
        )
        Language.click()
        time.sleep(6)
        print("Test case 20: Directed to TV Shows.")
    except Exception as e:
        print(f"An error occurred in test case 20: {str(e)}")

    try:
        driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[3]').click()
        driver.find_element(By.LINK_TEXT, "Sign out of Netflix").click()
        time.sleep(6)
        print("Test case 21: Logout.")
    except Exception as e:
        print(f"An error occurred in test case 21: {str(e)}")







except Exception as e:
    print(f"An error occurred: {str(e)}")

driver.quit()