# Excel - Checkpoint Configuration Backup Script

## ToC

- [Intro](#intro)
- [Compatibility](#requirements)
- [Compatibility](#compatibility)
- [Configuration](#configuration)
- [Usage](#usage)


## Intro

This is a python script to backup Checkpoint MDS Devices

This is developed as Ansible lacks the ability to support Checkpoint device.

Script can be run via CLI or through Ansible "script" module

## Requirements

The following requirements must be installed to use this Inventory Script:

- [Python](https://www.python.org/) - Python3 programming language
- [SCP](https://pypi.org/project/scp/) - A Python library that leverage on paramiko transport to send and receive files via scp protocol

## Compatibility

- Python3

Tested on Ansible 2.7.11 and below.

Does not work with Ansible 2.8 due to a bug in 2.8 which causes executing of python file to fail

## Configuration

To make use of 'checkpoint_config_backup.py' you must first have the following information

- checkpoint device ip
- checkpoint ssh username
- checkpoint ssh password
- host backup config directory
- desired config filename (must end with .tar.gz)
	


## Usage

### Bash
```bash
python ./checkpoint_config_backup.py 192.168.1.1 username password /home/backup cp_backup.tar.gz
```

### Ansible Playbook
```yaml
- name: Run checkpoint backup script
  script: "checkpoint_config_backup.py 192.168.1.1 username password /home/backup cp_backup.tar.gz"
  register: log
  delegate_to: localhost
```