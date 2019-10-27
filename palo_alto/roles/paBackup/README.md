Palo Alto Configuration Backup
=========

This role will take configuration of Palo Alto device via it's api interface and transfer to FTP server for archiving

## Requirements
- Ansible Tower
- Ansible Galaxy

## Role Variables
 - ansible_user ( login username )
 - ansible_password ( login password )
 - ansible_host ( IP address )
 
## Playbook
Import this role with the following playbook
```
- name: Palo Alto
  hosts: palo_alto
  gather_facts: no
  
  roles:
  - paBackup
```
