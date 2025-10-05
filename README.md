# Rellenar Google Forms automáticamente desde Firefox

Pequeño script en Python para rellenar un Google Form de manera automática.  
Puede utilizarse para rellenar cualquier formulario web, pero se deben modificar los nombres, `jsname` o tipos de cada elemento según el formulario.

---

## 🔧 Requisitos

1. **Instalar geckodriver**  
   Descárgalo desde: [Geckodriver Releases](https://github.com/mozilla/geckodriver/releases)  

2. **Instalar Selenium**  
   Ejecuta en la terminal o PowerShell:
   ```bash
   pip install selenium
   ```

## 💻 Descargar y configurar el script mediante el Programador de tareas

1. **Descargar y preparar el script**  
   - Descarga el script.
   - Modifica los valores según tu formulario: cada Google Form tiene nombres, `jsname` o atributos diferentes para `textarea`, `input`, `button`, etc.  
   - Puedes hacerlo de dos maneras:  
     - **Manual:** inspeccionando el formulario con el navegador y ajustando los XPaths o atributos en el script.  
     - **Automático:** usando scraping para detectar y asignar los campos dinámicamente.
       
   En este caso se ha hecho de forma manual porque es para un simple formulario que siempre mantiene los nombres, en caso de necesitarlo para
       algo más complejo, recomiendo la segunda opción.

- Configurar el programador de tareas via GUI
  Esto puede realizarse también por comando, pero nunca había usado el programador de tareas y he querido hacerlo usando la GUI.
  <img width="832" height="576" alt="imagen" src="https://github.com/user-attachments/assets/9b05ebcf-273c-40da-961b-6436c246497e" />
  <img width="1020" height="575" alt="imagen" src="https://github.com/user-attachments/assets/3ad73344-1816-4d51-82df-ae950fabc830" />
  <img width="918" height="552" alt="imagen" src="https://github.com/user-attachments/assets/ecfcaf4b-31a1-4fd1-8254-36d672873e46" />
  <img width="683" height="494" alt="imagen" src="https://github.com/user-attachments/assets/2cda2c39-cc1b-4335-b490-58c66b627bcb" />


  
