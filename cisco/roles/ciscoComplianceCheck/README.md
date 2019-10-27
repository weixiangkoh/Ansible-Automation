Cisco Routing and Switching Compliance Check
=========

This role will check if cisco device is in compliance with hardening guide and output a report in /home/generated_report.html

Requirements
------------
- Linux
- Ansible
- Ansible Galaxy

Role Variables
--------------

- hardening_check
- ansible_host (  device IP )
- ansible_user (  device ssh username )
- ansibile_password ( device ssh password)

*Update "hardening_check" variable in vars/main.yml"

Site.yml Playbook
----------------

---
- name: Cisco Playbook
  hosts: cisco
  gather_facts: no
  connection: local

  roles:
  - ciscoComplianceCheck
