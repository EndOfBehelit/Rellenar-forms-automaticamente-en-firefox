# instalar: pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ruta a geckodriver si no está en PATH
service = Service(r"C:\Users\USER\Downloads\geckodriver-v0.36.0-win32\geckodriver.exe")

opts = Options()
opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
opts.add_argument("--headless") # No abre la ventana de firefox

driver = webdriver.Firefox(service=service, options=opts)
driver.get("RUTA FORMS")

wait = WebDriverWait(driver, 10) #Esto sirve a que de tiempo a cargar la pagina, sino puede dar erorr al no encontrar algo que aun no ha cargado

# Correo
time.sleep(0.5)  # medio segundo
correo = driver.find_element(By.XPATH, '(//input[@jsname="YPqjbf"])[1]')
correo.send_keys("mi_correo@test.com")

# Nombre
time.sleep(0.5)  # medio segundo
correo = driver.find_element(By.XPATH, '(//input[@jsname="YPqjbf"])[2]')
correo.send_keys("Nombre de prueba")

# Checkbox1
opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="2"])[1]')
opcion.click()

# Checkbox2
opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="10"])[2]')
opcion.click()

# Checkbox3
opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="10"])[3]')
opcion.click()

# texto1
time.sleep(1)  # un segundo
correo = driver.find_element(By.XPATH, '(//textarea[@jsname="YPqjbf"])[1]')
correo.send_keys("Texto de prueba")

# Texto 2
time.sleep(0.5)  # medio segundo
correo = driver.find_element(By.XPATH, '(//textarea[@jsname="YPqjbf"])[2]')
correo.send_keys("Texto de prueba 2")

# Botón enviar
time.sleep(0.5)  # medio segundo
submit = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
submit.click()

# Cerrar firefox
driver.quit()

