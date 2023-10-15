import subprocess
import requests as request
import stem

tor_config = {'ControlPort': '9051', 'SocksPort': '5000'}
stem.process.launch_tor_with_config(config = tor_config, tor_cmd = '')
# Configuracion del proxy
proxy_config = {
    'http_proxy': 'http://127.0.0.1:9050',  # Cambia la dirección y el puerto según corresponda
    'https_proxy': 'http://127.0.0.1:9050',
}


def checkIp():
    res:str = ''
    req = request.get("http://ipinfo.io/json", proxies = proxy_config )
    res = req.json()
    return res


print(checkIp())

# Ejecuta un comando en la terminal
def download():
    url = "https://mega.nz/folder/ddUlHLSS#zCj0yBi8kWAw-DYCJs7Aag/file/ZAtSkYLQ"


    comando = "mega-get " + url  # Descargar por medio de url



    proceso = subprocess.Popen(
        comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=proxy_config
    )




    # Captura la salida estándar y la salida de error del comando
    salida, error = proceso.communicate()

    # Imprime la salida del comando
    print("Salida:")
    print(salida.decode("utf-8"))

    # Imprime la salida de error, si la hubiera
    if error:
        print("Error:")
        print(error.decode("utf-8"))
