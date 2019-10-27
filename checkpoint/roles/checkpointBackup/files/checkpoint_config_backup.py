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
save_file_path = sys.argv[4]
desired_filename = sys.argv[5]
port = 22


class ftpException(Exception):
    pass


class sshException(Exception):
    pass


def connect_to_host():
    print "Connecting to %s" %(ip)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=username, password=password, allow_agent=False, look_for_keys=False)
    print "Connected to %s" % (ip)
    return client


def get_filename(output):
    print "Grabbing filename from output"
    print output
    file = output.split("successfully:", 1)[1]
    file = file.translate(None, "()")
    file = file.split("/")
    filename = file[-1].split()[0]
    print "Filename : %s" %(filename)
    return filename


def wait_command_end(chan):
    print "Waiting for backup to complete"
    log, outdata, errdata = '', '',''
    while True:  # monitoring process
        # Reading from output streams
        while chan.recv_ready():
            outdata = chan.recv(1000)
            #print outdata
            log += outdata
        while chan.recv_stderr_ready():
            errdata += chan.recv_stderr(1000)
        if chan.exit_status_ready():  # If completed
            break
        time.sleep(0.001)
    return log


def retrieve_file(sshclient, filename):
    with SCPClient(sshclient.get_transport())as scp:
        dest = save_file_path + desired_filename
        scp.get("./" + filename, dest)
    print "File Transfer Completed"


def remove_from_device(ssh_transp, filename):
    chan = ssh_transp.open_session()
    chan.setblocking(0)
    print "Removing backup file from device"
    chan.exec_command('rm -rf %s' % (filename))
    print "File removed from device"
    chan.close()

def initate_backup(ssh_transp):
    chan = ssh_transp.open_session()
    chan.setblocking(0)
    chan.exec_command("mds_backup -l\n")
    chan.send("y")
    chan.send("\n")
    chan.send("\n")
    chan.send("\n")
    return wait_command_end(chan)

def start_mds(ssh_transp):
    chan = ssh_transp.open_session()
    chan.setblocking(0)
    chan.exec_command("mdsstart\n")
    wait_command_end(chan)

def start_backup(sshclient):
    print "Starting backup of Checkpoint MDS"
    ssh_transp = sshclient.get_transport()
    logs = initate_backup(ssh_transp)
    filename = get_filename(logs)
    start_mds(ssh_transp)
    retrieve_file(sshclient,filename)
    remove_from_device(ssh_transp,filename)
    print("Done")
    ssh_transp.close()

def main():
    sshclient = connect_to_host()
    start_backup(sshclient)
    sshclient.close()


if __name__ == "__main__":
    main()
