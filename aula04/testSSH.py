#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.0.2")
stdin,stdout,stderr = ssh.exec_command("ls -la")
print stdout.read()

if stderr.channel.recv_exit_status != 0:
    print stderr.read()
else:
    print stdout.read()
