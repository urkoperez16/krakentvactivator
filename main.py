import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = 'YOUR PATH'

def interact_with_buttons():
    driver = webdriver.Chrome(executable_path=driver_path)
    
    url = 'https://www.listasiptvactualizadas.com/activar-kraken-tv.php?token=XGQNP8'
    driver.get(url)
    
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.ID, 'btnactiv_b9155cafda96f5c2')))

    button1 = driver.find_element(By.ID, 'btnactiv_b9155cafda96f5c2')
    button1.click()

    time.sleep(2)

    # Realiza acciones (hacer clic en el segundo botón)
    button2 = driver.find_element(By.ID, 'btnactiv_7da3fee9264186b1')
    button2.click()

    time.sleep(5)

    driver.quit()

interact_with_buttons()

while True:
    time.sleep(1800)  # 1800 segundos = 30 minutos
    interact_with_buttons()
