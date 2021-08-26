# import paramiko
# ssh_client=paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=portal.iidf.ru, key_filename='/home/leonid/.ssh/frii.ppk')

# stdin, stdout, stderr = ssh_client.exec_command('ls')
# ssh_client.close()

#!/usr/bin/python3.8
import subprocess
import sys

def send_photos(photo):
	subprocess.run(["scp", "-i", "/home/leonid/.ssh/frii.ppk", f"./employees_photos/{photo}", "portal.iidf.ru:/var/www/html/portal/photos/"])

if __name__ == '__main__':
	send_photos(sys.argv[1])