#!/bin/python3

import sys
import socket
from datetime import datetime
import threadin

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
    except:
        pass

if len(sys.argv) != 2:
    print("Syntax: python3 scanner.py <target>")
    sys.exit()

target = socket.gethostbyname(sys.argv[1])

print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

threads = []

try:
    for port in range(1, 1025):  # Scan ports from 1 to 1024
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()

