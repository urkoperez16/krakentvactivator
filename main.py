import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta al controlador descargado
driver_path = '/home/urko/Descargas/chromedriver_linux64/chromedriver'

def interact_with_buttons():
    # Inicializa el navegador
    driver = webdriver.Chrome(executable_path=driver_path)

    # Abre la página
    url = 'https://www.listasiptvactualizadas.com/activar-kraken-tv.php?token=XGQNP8'
    driver.get(url)

    # Espera hasta que los elementos estén presentes
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.ID, 'btnactiv_b9155cafda96f5c2')))

    # Realiza acciones (hacer clic en el primer botón)
    button1 = driver.find_element(By.ID, 'btnactiv_b9155cafda96f5c2')
    button1.click()

    # Espera hasta que el segundo botón esté presente
    element = wait.until(EC.presence_of_element_located((By.ID, 'btnactiv_7da3fee9264186b1')))

    # Realiza acciones (hacer clic en el segundo botón)
    button2 = driver.find_element(By.ID, 'btnactiv_7da3fee9264186b1')
    button2.click()

    # Cierra el navegador al finalizar
    driver.quit()

# Programa la ejecución cada 30 minutos
schedule.every(30).minutes.do(interact_with_buttons)

# Ejecuta la planificación
while True:
    schedule.run_pending()
    time.sleep(1)
