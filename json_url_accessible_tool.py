#!/usr/bin/python3
import requests
import sys
import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="Check json URL accessible tool")
parser.add_argument("-apk", type=str, help="Enter apk file", required=True)

a = parser.parse_args()
#h = sys.argv[1]+"/.json"
h = sp.getoutput("strings {} | egrep -o https\:\/\/\(.*\).firebaseio.com ".format(a.apk))
url = ("{}/.json".format(h))
print (h)
r=requests.get(url)
if r.status_code == 200:
    print("Readable")
else:
    print("Non-Redable")


payload={'text':'anything'}
r=requests.put(h,data=payload)
if r.status_code == 201 or r.status_code == 200:
    print("Writable")
else:
    print("Can't write")
