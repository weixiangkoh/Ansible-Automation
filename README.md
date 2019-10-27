# Ansible-Automation
Most of the playbooks are full-fledged end to end workflow, which use Ansible as a configuration management automation tool to ease the provisioning, configuring and checking of 
Vmware vSphere, Cisco, F5, Palo Alto, Juniper and Checkpoint. Not all playbooks follow all of Ansible's best practices, as they illustrate particular use case in an instructive manner.


## Quick Start
- [System Requirement](#requirement)
- [Ansible Installation](#installation-ansible)
- [Clone this repo](#Git)
- [Setup Inventory](#setup-inventory)


## System Requirement
- Rhel 7 / Centos 7 =<
- Minimum 2 CPU though based on recommended specs, 4 CPU is ideal for the start
- Minimum 3 GB RAM incremental based on 10 host/1GB calculation

Installation guides for other linux system can be retrieved here [Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

## Ansible Installation
You will need to install Redhat epel-release before installing ansible
```
yum -y update
yum -y install epel-release
yum -y install ansible
```

## Clone this Repo
```
git clone https://github.com/weixiangkoh/Ansible-Automation.git
```

## Setup Inventory
Using your preferred linux editor (vim / nano)
Inventory should look something like this
```
[cisco]
nxos1 ansible_host=x.x.x.x ansible_network_os=nxos ansible_user=username ansible_password=password
```
