# F5 Bigip Configuration Backup
This role will backup F5 Bigip Configuration and save it to /tmp/ in ansible node

## Requirements
- Ansible Tower
- Ansible Galaxy

## Role Variables
- ansible_host ( IP of F5 device )
- ansible_user ( F5 Login username )
- ansible_password ( F5 Login password )

## Playbook
Import this role with the following playbook
```
- name: F5 Playbook
  hosts: F5
  gather_facts: no

  roles:
  - f5Backup
```