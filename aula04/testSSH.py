#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko

ssh = SSHClient()

ssh.client_load_system_host_keys()
ssh.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ssh.connect("192.168.0.2")
