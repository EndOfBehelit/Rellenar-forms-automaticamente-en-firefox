# instalar: pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # ruta a geckodriver si no está en PATH
    service = Service(r"C:\Users\Carba\OneDrive - Universidad de Oviedo\Escritorio\Test rellenar form\geckodriver-v0.36.0-win32\geckodriver.exe")

    opts = Options()
    opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    opts.add_argument("--headless") # No abre la ventana de firefox

    driver = webdriver.Firefox(service=service, options=opts)
    driver.get("https://docs.google.com/forms/d/1cnzlScPsOeQBWDC65IPc7caZGXQmTP4JzNEk1AAdJ7E/edit")

    wait = WebDriverWait(driver, 10) #Esto sirve a que de tiempo a cargar la pagina, sino puede dar erorr al no encontrar algo que aun no ha cargado

    print("Rellenando formulario...")
    # Correo
    time.sleep(0.5)  # medio segundo
    correo = driver.find_element(By.XPATH, '(//input[@jsname="YPqjbf"])[1]')
    correo.send_keys("jorcarmor@hotmail.com")

    # Nombre
    time.sleep(0.5)  # medio segundo
    correo = driver.find_element(By.XPATH, '(//input[@jsname="YPqjbf"])[2]')
    correo.send_keys("Carba")

    # Cansancio
    opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="2"])[1]')
    opcion.click()

    # Dormir
    opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="10"])[2]')
    opcion.click()

    # Comer
    opcion = driver.find_element(By.XPATH, '(//div[@role="checkbox" and @aria-label="10"])[3]')
    opcion.click()

    # Lesion hoy
    time.sleep(1)  # medio segundo
    correo = driver.find_element(By.XPATH, '(//textarea[@jsname="YPqjbf"])[1]')
    correo.send_keys("No")
    #correo.send_keys("Sin lesion")

    # Lesion pasada
    time.sleep(0.5)  # medio segundo
    correo = driver.find_element(By.XPATH, '(//textarea[@jsname="YPqjbf"])[2]')
    correo.send_keys("No")
    #correo.send_keys("Sin lesion pasada")

    # Botón enviar
    time.sleep(0.5)  # medio segundo
    submit = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
    submit.click()
    
except:
    print("Ha ocurrido algún error.")
else:
    print("Todo rellenado sin problemas")
# cerrar explorador
driver.quit()
