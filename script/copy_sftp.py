'''
    Option 1 Using pysftp
    Note that you would need to establish the sftp connection once manually for this to work.
    As doing the sftp connection manually updates the known_host file under .ssh directory with the sftp hostname
'''
import pysftp
from datetime import datetime

hostname = 'sftp1-uw2a-dev-tangerine.syapse.com'
username = 'cloverleaf-user'
password = 'ZL2QbD4ghheOHNsOV0q14h30wpyV5ORfFo8MCtYtClTjDSciTE31fo08atD5HM6v'

with pysftp.Connection(hostname, username=username, password=password) as sftp:
    print('Connection established')

    print('The file got copied at SFTP location at {}'.format(datetime.now()))

    localFilePath = './provider_aurora_1.csv'
    remoteFilePath = '/files/extracts/AURORA/provider_aurora_1.csv'

    sftp.put(localFilePath, remoteFilePath)

    sftp.cwd('/files/extracts/AURORA')

    dir_str = sftp.listdir_attr()
    file = [attr.filename for attr in dir_str]

    while localFilePath[2:] in file:

        dir_str = sftp.listdir_attr()
        file = [attr.filename for attr in dir_str]

        print(file)

    print('The file got picked up at {}'.format(datetime.now()))

'''
    Option 2: Use paramiko
    This code is more flexible and can be executed from any machine without updating known host file
'''

import paramiko
from datetime import datetime

hostname = 'sftp1-uw2a-dev-tangerine.syapse.com'
username = 'cloverleaf-user'
password = 'ZL2QbD4ghheOHNsOV0q14h30wpyV5ORfFo8MCtYtClTjDSciTE31fo08atD5HM6v'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, username=username, password=password)
    print('Connection established')
except paramiko.SSHException as e:
    print ("Connection Error: " + e)

localFilePath = './provider_aurora_1.csv'
remoteFilePath = '/files/extracts/AURORA/provider_aurora_1.csv'

sftp = ssh.open_sftp()
print('The file got copied at SFTP location at {}'.format(datetime.now()))
sftp.put(localFilePath, remoteFilePath)

sftp.chdir("/files/extracts/AURORA/")
dir_str = sftp.listdir_attr()

file = [attr.filename for attr in dir_str]

while localFilePath[2:] in file:
    dir_str = sftp.listdir_attr()
    file = [attr.filename for attr in dir_str]
    print(file)

print('The file got picked up at {}'.format(datetime.now()))

ssh.close()