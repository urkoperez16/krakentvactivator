import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'YOUR PATH'

def interact_with_buttons():
    driver = webdriver.Chrome(executable_path=driver_path)
    
    url = 'https://www.listasiptvactualizadas.com/activar-kraken-tv.php?token=YOUR TOKEN'
    driver.get(url)
    
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.ID, 'YOUR BOTTOM')))

    button1 = driver.find_element(By.ID, 'YOUR BOTTOM')
    button1.click()

    time.sleep(2)

    # If you have 2 devices delete next #
    #button2 = driver.find_element(By.ID, 'YOUR BOTTOM 2')
    #button2.click()
    #time.sleep(5)

    driver.quit()

interact_with_buttons()

while True:
    time.sleep(1800)  # 1800 segundos = 30 minutos
    interact_with_buttons()
