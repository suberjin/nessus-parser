# NESSUS REPORT PARSER
--------------------------------------

## Description

This parser is a PoC. The files centos.py and ubuntu.py parse output of Nessus plugins by specific patterns 
and return list of packages that need to be updated in JSON format. The scripts need 2 arguments: host ip 
and name of csv file.

In addition, repository has an ansible playbook that uses the aforementioned files in order to update vulnerable 
packages.


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
