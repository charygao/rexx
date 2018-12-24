import urllib.request
import urllib.error
import time
import socket
import keyboard
from multiprocessing import Pool

domain = ""

def main(target):
    global domain
    domain = target
    start = time.time()
    file = open('modules/engine/sublist.txt', 'r', encoding="ISO-8859-1") #
    subdomains = file.readlines()

    non_blank_count = 0

    with open('modules/engine/sublist.txt') as infp:
        for line in infp:
            if line.strip():
                non_blank_count += 1

    print("\n Loaded dictionary module - " + str(non_blank_count) + " hosts")
    try:
        p = Pool(processes=20) #
        result = p.map(checkurl, subdomains)
    except socket.timeout:
        pass
    print(" Time: ", str(time.time()-start)[:-12] + " seconds")


def checkurl(url):
    try:
        check = url[:-1] + "." + domain
        conn = urllib.request.urlopen("http://" + check, timeout=5)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        try:
            ip = socket.gethostbyname(check)
            print(" " + check + " - " + ip)
        except socket.timeout:
            pass

    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        pass
    else:
        # 200
        try:
            ip = socket.gethostbyname(check)
            print(" " + check + " - " + ip)
        except socket.timeout:
            pass
