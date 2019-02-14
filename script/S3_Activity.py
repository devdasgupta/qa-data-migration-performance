import boto3
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
                msg_list.append('{} 1 {}'.format(self.bucket_name + ':' + fname, tstamp))

        return msg_list


if __name__ == "__main__":
    main()