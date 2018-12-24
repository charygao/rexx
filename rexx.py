import requests
import json
import shodan
import socket
import dns.resolver
banner = """
             _ __ _____  ____  __
            | '__/ _ \ \/ /\ \/ /
            | | |  __/>  <  >  <
            |_|  \___/_/\_\/_/\_\

                  Jake Bolam

"""
print(banner)

# Need to filter out http:// + https:// + www.

target = input(" Domain: ")


try:
    print("\n Nameservers:")
    answers = dns.resolver.query(target,'NS')
    for server in answers:
        st = str(server.target)
        ip = socket.gethostbyname(st)
        print(" " + st[:-1] + " - " + ip) #removes . from end of nameservers and appends IP
except:
    print(" Error - please check your domain and internet connection.")
    exit()


print ("\n Starting Subdomain Engine: done")

from modules.engine import dictionary, virustotal
dictionary.main(target)
virustotal.main(target)
