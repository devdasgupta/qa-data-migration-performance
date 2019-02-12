import uuid
import boto3
import socket
from datetime import datetime


class S3Activity:

    def __init__(self, bucket_name, profile):
        self.bucket_name = bucket_name
        self.profile = boto3.session.Session(profile_name=profile)
        self.s3_resource = self.profile.resource('s3')

    def upload_s3(self, filename, report_folder):

        bucket = self.s3_resource.Bucket(name=self.bucket_name)
        full_path = report_folder.strip() + filename.strip()

        s3_object = self.s3_resource.Object(bucket.name, full_path)
        s3_object.upload_file(filename)

    def get_s3_details(self, folder):
        bucket = self.s3_resource.Bucket(name=self.bucket_name)

        msg_list = list()

        for obj in bucket.objects.all():
            fname = obj.key
            if fname.startswith(folder):
                s3_obj = self.s3_resource.Object(self.bucket_name, fname)
                tstamp = int(datetime.strptime(str(s3_obj.last_modified), '%Y-%m-%d %H:%M:%S+00:00').strftime("%s"))
                msg_list.append('{} 1 {}'.format(self.bucket_name, tstamp))

        return msg_list


class GraphiteClient:

    def __init__(self, host):
        self.host = host
        self.port = 2003
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_message(self, name, value, tstamp):
        graphite_msg = "%s %s %s\n" % (name, value, tstamp)
        self.sock.sendall(graphite_msg.encode('utf-8'))

    def __del__(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except Exception as e:
            self.sock.close()
            print('Socket Exception: ' + str(e))


class TestExecution(S3Activity, GraphiteClient):

    def __init__(self, bucket_name, profile, host='localhost'):
        GraphiteClient.__init__(self, host)
        S3Activity.__init__(self, bucket_name, profile)

    def create_temp_file(self, size, file_name, file_content):
        random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
        with open(random_file_name, 'w') as f:
            f.write(str(file_content) * size)
        return random_file_name

    def __del__(self):
        GraphiteClient.__del__(self)


def main():
    profile = 'dev'
    cloverleaf = TestExecution('syapse-performance-results', profile)
    folder = 'Test_Upload/'

    for i in cloverleaf.get_s3_details(folder):
        item = i.split()
        path = 'Metrics.Test.' + item[0].replace('.', '-')
        print(item[0], item[1], item[2])
        cloverleaf.send_message(path, item[1], item[2])

    del cloverleaf


if __name__ == '__main__':
    main()