# NESSUS REPORT PARSER
--------------------------------------

## Description

This parser is a PoC. The files centos.py and ubuntu.py parse output of Nessus plugins by specific patterns 
and return list of packages that need to be updated in JSON format. The scripts need 2 arguments: host ip 
and name of csv file.

In addition, repository has an ansible playbook that uses the aforementioned files in order to update vulnerable 
packages.

## Project structure

The project has the following files:

- README.md -- readme
- centos.py -- parser for CentOS. The python script that parses Nessus plugin output and finds patterns taht could be used to receive list of vulnarable packages. Returns JSON that could be used in order to create template for Ansible
- ubuntu.py -- parser for Ubuntu. The python script that parses Nessus plugin output and finds patterns taht could be used to receive list of vulnarable packages. Returns JSON that could be used in order to create template for Ansible
- main.yaml -- main Ansible playbook. It contains tasks that run parses according to `ansible_distribution`, get JSON and creates list of packages that need to be updated.
- inventory.ini -- inventory file. Contains list of hosts that need ot be chacked in report
- report.csv -- Nessus report. On this stage it has been received from Nessus manually
- requirements.txt -- list of python requirements


## Requirements

Supported OS:
- Ubuntu
- CentOS

Packages:
- python3
- ansible

The packages could be installed via:

```pip install -r requirements.txt```

## TODO

- This parser needs more tests.
- It is necessary to configure notifications about updated packages. We also need log update reports.
- We need to check a package before update in CVS databases in order to make sure that the new package
doesn't have more serious vulnerabilities.
