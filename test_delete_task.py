from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_delete_task():
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000')

    # Select and delete the first task
    driver.find_elements(By.NAME, 'taskCheckbox')[0].click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]").click()
    time.sleep(1)

    # Verify task is deleted
    tasks_elements = driver.find_elements(By.TAG_NAME, 'li')
    assert len(tasks_elements) == 2

    driver.quit()
