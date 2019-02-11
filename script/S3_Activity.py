import boto3


class S3Activity:

    def __init__(self, bucket_name, profile):
        self.bucket_name = bucket_name
        self.profile = boto3.session.Session(profile_name=profile)
        self.s3_resource = self.profile.resource('s3')

    @staticmethod
    def upload_s3(self, filename, report_folder):

        bucket = self.s3_resource.Bucket(name=self.bucket_name)
        full_path = report_folder + filename

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

if __name__ == "__main__":
    main()