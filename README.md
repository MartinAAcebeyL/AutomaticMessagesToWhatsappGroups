# Proyecto de envío de SMS a WhatsApp con Python, Selenium, Chrome y la API de Drive
Este proyecto tiene como objetivo automatizar el envío de mensajes de texto a través de WhatsApp utilizando Python, la biblioteca Selenium, el navegador Chrome y la API de Drive de Google. El proceso implica el uso de Selenium para interactuar con WhatsApp Web, enviar mensajes a través de Chrome y utilizar la API de Drive para almacenar y recuperar datos.


## Requisitos
Para ejecutar este proyecto, necesitarás los siguientes requisitos previos:
1. Python 3.7 o superior
2. Selenium
3. Navegador Chrome
4. Cuenta de Google: Necesitarás una cuenta de Google para acceder a la API de Drive. Puedes crear una cuenta de forma gratuita en el sitio web de Google.
5. Credenciales de API de Google Drive: Necesitarás obtener las credenciales de la API de Google Drive para acceder a tus archivos en Drive. Sigue los siguientes pasos:
    * Visita el [sitio web](https://console.cloud.google.com/projectselector2/apis/dashboard?supportedpurview=project) de desarrolladores de Google.
    * Crea un nuevo proyecto o selecciona uno existente.
    * Habilita la API de Drive para el proyecto.
    * Configura las credenciales de API y descarga el archivo JSON que contiene las credenciales.
6. Chrome WebDriver: Descarga el [Chrome WebDriver](https://chromedriver.chromium.org/downloads) compatible con tu versión de Chrome desde el sitio web oficial de Selenium WebDriver.
7. Archivos del proyecto: Además de los requisitos previos, asegúrate de tener los siguientes archivos en tu proyecto:
    * credenciales.json: Archivo JSON que contiene las credenciales de la API de Google Drive.
## Configuración e instalación
1. Clona el repositorio en tu computadora con:

    ```git clone https://github.com/MartinAAcebeyL/AutomaticMessagesToWhatsappGroups.git```
2. Crea un entorno virtual con el comando 

    `python3 -m venv venv`
3. Activa el entorno virtual con el comando 

    `source venv/bin/activate`
4. Instala las dependencias del proyecto con el comando 

    `pip install -r requirements.txt`

5. Coloca el archivo JSON con las credenciales de la cuenta de servicio de la API de Drive en la raiz del proyecto, con el nombre credentials.json.
6. Define los números de teléfono o nombres a los que deseas enviar mensajes en [aqui](contacts.txt). Por ejemplo:

    ```
    12345678
    Perico perez
    Grupo de compra/venta
    ```
7. Crea un archivo .env con las indicaciones del archivo [.env.example](.env.example).
8. Crear una carpeta llamada selenium en la raiz del proyecto, aqui se guardaran sesiones, entre otras muchas cosas para por ejemplo no tener que scanear el Qr de Whatsapp.

## Uso del proyecto
1. Ejecuta el archivo app.py para iniciar el envío de SMS a través de WhatsApp.

    ```python app.py```
2. La primera vez que ejecutes el proyecto, se abrirá una ventana del navegador Chrome y se te pedirá que inicies sesión en tu cuenta de Google. Inicia sesión con la cuenta que contiene el archivo JSON con las credenciales de la API de Drive.
3. Una vez que hayas iniciado sesión, se te pedirá que permitas que la aplicación acceda a tu cuenta de Google. Haz clic en el botón Permitir para continuar.
4. Se abrirá una nueva ventana del navegador Chrome y se te pedirá que escanees el código QR de WhatsApp. Escanea el código QR con tu teléfono móvil para iniciar sesión en WhatsApp Web.
5. Obtendras un panel donde tendras en control para enviar archivos de determinada carpeta o enviar de todas las carpetas.
5. El proyecto leerá los números de teléfono de contacts.txt.
6. Observa el navegador Chrome abierto por Selenium mientras se envían los mensajes. No interactúes con el navegador durante el proceso de envío.
7. Una vez que se hayan enviado todos los mensajes, el programa volvera al panel principal.

## Consideraciones adicionales
* Asegúrate de tener una conexión a Internet estable para que el proyecto funcione correctamente.
* El ID de la carpeta de donde leera los archivos, carpetas y multimedia debe estar estructurado de la siguiente manera: 
    ```
    Carpeta principal/
    ├── Carpeta 1
    │   ├── fotos
    │   ├── videos
    │   ├── name1.txt
    │   ├── name2.txt
    │   └── name3.txt
    │   └── ....txt
    ├── Carpeta 2
    |   ├── fotos
    │   ├── videos
    │   ├── name1.txt
    │   ├── name2.txt
    │   └── name3.txt
    │   └── ....txt
    ├── Carpeta 3
    |   ├── fotos
    │   ├── videos
    │   ├── name1.txt
    │   ├── name2.txt
    │   └── name3.txt
    │   └── ....txt
    └── ....
    ```
* Ten en cuenta que el uso excesivo o abusivo de esta herramienta puede violar los términos de servicio de WhatsApp y puede tener consecuencias legales.
* Este proyecto es solo con fines educativos y se proporciona tal como está, sin garantías de ningún tipo.

## Licencia
Este proyecto está bajo la Licencia MIT. Si utilizas o te inspiras en este proyecto, se agradece pero no es obligatorio, que menciones la autoría.

Espero que este README te ayude a comprender el proyecto y cómo utilizarlo. ¡Diviértete enviando mensajes SMS a través de WhatsApp!