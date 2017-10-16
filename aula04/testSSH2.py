#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko
from datetime import datetime,timedelta

hosts = ["192.168.0.1","192.168.0.2","192.168.0.3"]


ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for h in hosts:
    try:
        print "Conectando no servidor %s na data %s"%(h,datetime.now())
        ssh.connect(h)
        stdin,stdout,stderr = ssh.exec_command("w")
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print stdout.read()
        print "Saindo do servidor %s na data %s"%(h,datetime.now())
    except Exception as e:
        print "Nao conseguiu conectar ao servidor %s"%e
