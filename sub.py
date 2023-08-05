import requests
from time import sleep
from prettytable import PrettyTable
from termcolor import colored

def check_domains_status(domainsname):
    tableformat = PrettyTable()
    tableformat.field_names = ["Domain", "Status"]
    for A in domainsname:
      try:
          statlocalhost = requests.get("http://"+A)
          if statlocalhost.status_code == 200:
            tableformat.add_row([A, colored("UP", "green")])
          elif statlocalhost.status_code != 200:
             tableformat.add_row([A, colored("Down", "red")])
      except(requests.exceptions.RequestException, requests.exceptions.Timeout):
            tableformat.add_row([A, colored("DOWN", "red")])
    print(tableformat)
domainsname = ["localhost", "awesomeweb","123"]
while True:
    check_domains_status(domainsname)
    sleep(60)
   
