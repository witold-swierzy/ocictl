# OCICTL. A simple command-line tool for accessing database and compute resources
aaa
OCI Cli offers a command line interface to work with OCI resources, like compute instances, databases and object storage. However - as it uses JSON as a basic format for providing/getting data, its direct usage may seem, in some simpler cases, a bit unfriendly

OCICTL is a tool, which uses in the background standard OCI Cli interface, but instead of forcing using JSON it accepts more user-friendly, text ways of providing/getting required data

## Requirements:
### Python 3.* 
### OCI CLI installed and configured
### bash shell

Review Date: 28.01.2024

## Documentation
- [OCI Cli official documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)

## Usage
### to list all autonomous databases
ocictl.sh adb     list<p>
### to start an autonomous database
ocictl.sh adb start <display-name><p>
### to stop an autonomous database
ocictl.sh adb stop <display-name><p>
### to list all base database services
ocictl.sh adb     list<p>
### to start a base database service
ocictl.sh adb start <display-name><p>
### to stop a base database service
ocictl.sh adb stop <display-name><p>
### to list compute instances
ocictl.sh compute list
### to start a compute instance
ocictl.sh compute start <display-name>
### to stop a compute instance
ocictl.sh compute stop <display-name>
### to list existing Object Store buckets
ocictl.sh os bucket list
### to create a bucket
ocictl.sh os bucket create <bucket-name>
### to delete a bucket
ocictl.sh os bucket delete <bucket-name>
### to list files stored in a bucket
ocictl.sh os file list <bucket-name>
### to upload a file into a bucket
ocictl.sh os file put <bucket-name> <file-name>
### to download a file from a bucket
ocictl.sh os file get <bucket-name> <file-name>
### to start a group of resources
ocictl.sh group start <group-name>
### to stop a group of resource
ocictl.sh group stop <group-name>
### to list existing groups
ocictl.sh group list
# License

Copyright (c) 2023 Oracle and/or its affiliates.

Licensed under the Universal Permissive License (UPL), Version 1.0.

See [LICENSE](https://github.com/oracle-devrel/technology-engineering/blob/main/LICENSE) for more details.
