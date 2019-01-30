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
