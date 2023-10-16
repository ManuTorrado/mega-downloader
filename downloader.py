import subprocess
import requests as request
import stem.process
import json

import requests


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)

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
