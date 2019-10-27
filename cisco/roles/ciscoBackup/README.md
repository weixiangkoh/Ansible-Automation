# Ansible - Cisco IOS and ACI Configuration Backup Playbook

## ToC

- [Intro](#intro)
- [Compatibility](#requirements)
- [Compatibility](#compatibility)
- [Configuration](#configuration)
- [Usage](#usage)


## Intro

This is a ansible playbook to backup Cisco ACI and IOS configuration


## Requirements

The following requirements must be installed to use this Playbook:

- [Python](https://www.python.org/) - Python3 programming language
- [SCP](https://pypi.org/project/scp/) - A Python library that leverage on paramiko transport to send and receive files via scp protocol

## Compatibility

- Python3

Tested on Ansible 2.7.11 and below.


## Configuration

To use this playbook the following information must be specified before run ( edit the main.yml file in vars folder )

- ansible_network_os ( "ios" or "aci" )
- ansible_user ( ssh username )
- ansible_password ( ssh password )
- path ( host backup config directory )
- filename ( desired config filename )
	
### site.yml
```yaml
---
- name: Cisco Playbook
  hosts: cisco
  gather_facts: no
  connection: local

  roles:
  - ciscoBackup
```

## Usage

### Bash
```bash
ansible-playbook site.yml -u username --ask-pass
```