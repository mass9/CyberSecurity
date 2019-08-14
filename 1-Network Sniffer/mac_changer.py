#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:66:55:42"

print("[+] Changing MAC address for " + interface + "to " + new_mac)

subprocess.call("ifconfig " + interface +"down ", shell=True)
subprocess.call("ifconfig " + interface +"hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +"up ", shell=True)

