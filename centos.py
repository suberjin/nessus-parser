from csv import DictReader 
from sys import argv
from ipaddress import ip_address
from json import dumps
from re import search

# vaildate IP in args
try:
    ip = ip_address(argv[1])
except ValueError:
    print('address/netmask is invalid: %s' % argv[1])
except:
    print('Usage : %s  ip' % argv[0])

# define variables
HOST = argv[1]
filename = argv[2]

# initializing variables
initial = []
package_set = set()

# reading csv file 
with open(filename, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = DictReader(csvfile)

    # extracting each data row one by one 
    for row in csvreader:
        if row["Host"] == HOST and "Should be" in row["Plugin Output"]:
           plugin_output = row["Plugin Output"].split("\n")
           for i in plugin_output:
               if i.find("Should be") != -1:
                   plugin_output_splited=i.split(":",maxsplit=1)
                   row_package=plugin_output_splited[1].lstrip()
                   row_spliter=search(r"-(\d+)",row_package)
                   package=row_package[:row_spliter.start()]
                   package_set.add(package)

# creating json
for i in package_set:
    initial.append({'package':i})

print(dumps(initial))
