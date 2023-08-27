import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta al controlador descargado
driver_path = 'YOUR PATH'

def interact_with_buttons():
    # Configura las opciones del controlador
    chrome_options = Options()

    # Inicializa el controlador
    driver = webdriver.Chrome(options=chrome_options)

    # Abre la página
    url = 'https://listasiptvactualizadas.com/activar-kraken-tv.php?token=YOUR TOKEN'
    driver.get(url)
    
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.presence_of_element_located((By.ID, 'YOUR BUTTON ID')))

    button1 = driver.find_element(By.ID, 'YOUR BUTTON ID')
    button1.click()

    # Espera 5 segundos
    time.sleep(5)

    # If you have 2 devices delete #
    #button2 = driver.find_element(By.ID, 'YOUR BUTTON ID')
    #button2.click()

    time.sleep(2)

    driver.quit()

while True:
    interact_with_buttons()
    time.sleep(1800)
