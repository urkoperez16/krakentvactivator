import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver_path = 'YOR PATH'

def interact_with_buttons():

    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://listasiptvactualizadas.com/activar-kraken-tv.php?token=YOUR TOKEN'
    driver.get(url)
    
    time.sleep(3)
    
    script = "document.querySelector('.fc-button.fc-cta-consent.fc-primary-button').click();"
    driver.execute_script(script)

    time.sleep(15)

    button1 = driver.find_element(By.ID, 'YOUR BUTTON ID')
    button1.click()
    
    print("✔ 1. Dispositivo Activado ✔")
    

    time.sleep(2)
    
    # IF YOU HAVE 2 DEVICES DELETED THIS #
    # button2 = driver.find_element(By.ID, 'YOUR SECOND BUTTON ID')
    # button2.click()
    
    # print("✔ 2. Dispositivo Activado ✔")

    # time.sleep(2)

    driver.quit()


while True:
    interact_with_buttons()
    time.sleep(1800)
