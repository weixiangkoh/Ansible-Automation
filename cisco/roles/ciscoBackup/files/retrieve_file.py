#!/usr/bin/env python

import sys, paramiko
import time
from scp import SCPClient

if len(sys.argv) < 5:
    print "args missing"
    sys.exit(1)

ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
filename = sys.argv[4]
path = sys.argv[5]
port=22

def send_command(client_cli, command):
    out = str()
    client_cli.send(command)
    while not client_cli.recv_ready():
       time.sleep(3)
    out = client_cli.recv(9999)
    print out

def connect_to_host():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,port,username ,password)
    print "connected to "+ip
    return client

def retrieve_file(sshclient):
    scp = SCPClient(sshclient.get_transport())
    scp.get("/data2/snapshots/"+filename,path+filename)
    print filename+" retrieved"
    scp.close()

def remove_snapshot(sshclient):
    client_cli = sshclient.invoke_shell()
    send_command(client_cli,'clear snapshot file '+filename+'\n')

def main():
    sshclient = connect_to_host()
    retrieve_file(sshclient)
    remove_snapshot(sshclient)
    sshclient.close()


if __name__== "__main__":
    main()
 