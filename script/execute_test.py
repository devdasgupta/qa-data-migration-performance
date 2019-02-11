import uuid
import boto3
import socket
import os


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

    def get_s3_details(self, bucket_name):
        bucket = self.s3_resource.Bucket(name=bucket_name)

        msg_list = list()

        for obj in bucket.objects.all():
            fname = obj.key
            s3_obj = self.s3_resource.Object(bucket_name, fname)
            msg_list.append('{} {} 1'.format(fname, s3_obj.last_modified))

        return msg_list


class GraphiteClient:

    def __init__(self, host):
        self.host = host
        self.port = 2003

    def graphite_connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        return sock

    def send_message(self, sock, path, msg):
        graphite_msg = "%s %s %d" % (path, msg, 1)
        sock.sendall(graphite_msg.encode('utf-8'))

    # def __del__(self, sock):
    #     try:
    #         sock.shutdown(socket.SHUT_RDWR)
    #         sock.close()
    #     except Exception as e:
    #         sock.close()
    #         print('Socket Exception: ' + str(e))


class TestExecution(S3Activity, GraphiteClient):

    def __init__(self, bucket_name, profile, host='localhost'):
        # super(TestExecution, self).__init__()
        GraphiteClient.__init__(self, host)
        S3Activity.__init__(self, bucket_name, profile)

    def create_temp_file(self, size, file_name, file_content):
        random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
        with open(random_file_name, 'w') as f:
            f.write(str(file_content) * size)
        return random_file_name


def main():
    profile = 'dev'
    cloverleaf = TestExecution('syapse-performance-results', profile)
    folder = 'Test_Upload/'

    for _ in range(20):
        filename = cloverleaf.create_temp_file(500, 'uploadfile.txt', 's')
        cloverleaf.upload_s3(filename, folder)
        os.remove(filename)


if __name__ == '__main__':
    main()