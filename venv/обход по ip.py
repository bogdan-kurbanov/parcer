import socks
import socket
import requests
from bs4 import BeautifulSoup
def checkIP():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    socket.socket = socks.socksocket
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)

checkIP()
