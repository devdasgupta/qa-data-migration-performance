import boto3
import json
from datetime import datetime
import time


REGION = 'us-west-2'
PROFILE = 'dev'

class kinesisActivity:

    def __init__(self, kinesis_stream, profile):
        self.kinesis_stream = kinesis_stream
        self.profile = boto3.session.Session(profile_name=profile)
        self.kinesis_client = self.profile.client('kinesis', REGION)

    def get_records(self):
        response = self.kinesis_client.describe_stream(StreamName = self.kinesis_stream)
        my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
        shard_iterator = self.kinesis_client.get_shard_iterator(StreamName=self.kinesis_stream, ShardId=my_shard_id, ShardIteratorType='LATEST')

        my_shard_iterator = shard_iterator['ShardIterator']
        record_response = self.kinesis_client.get_records(ShardIterator=my_shard_iterator, Limit=2)

        while 'NextShardIterator' in record_response:
            record_response = self.kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=2)
            print (record_response)

            time.sleep(5)


def main():

    my_kinesis = kinesisActivity('kinesis-dev-black-data-ingestion', PROFILE)
    my_kinesis.get_records()


if __name__ == "__main__":
    main()


