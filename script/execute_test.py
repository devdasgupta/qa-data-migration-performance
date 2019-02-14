import logging
import argparse
import time
from S3_Activity import S3Activity
from graphite_client import GraphiteClient
from datasetup import TestDataSetup
from utility import config as c


TIME_LIMIT = 30


def process_args():
    parser = argparse.ArgumentParser(description='Fake Data generator for Interop')
    parser.add_argument('customer', help='customer name')
    parser.add_argument('-p', 'pipeline', nargs='+', help='record or dataclass type')
    parser.add_argument(
        '--count', type=int, help='number of records to create (default 1)', default=1)
    arguments = parser.parse_args()
    return arguments


class TestExecution(S3Activity, GraphiteClient):

    def __init__(self, bucket_name, profile, host='localhost'):
        GraphiteClient.__init__(self, host)
        S3Activity.__init__(self, bucket_name, profile)

    def __del__(self):
        GraphiteClient.__del__(self)


def main():
    profile = 'dev'
    sftp_s3 = 'syapse-dev-sftp'
    cloverleaf = S3Activity(sftp_s3, profile)
    folder = 'files/extracts/AURORA/'
    filename = 'patient_1000.csv'

    # Create necessary file from Aurora using Cloversub utility


    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Starting the Phase I: Copying Data to SFTP location')
    logging.info('File placed in S3 bucket {}'. format(sftp_s3))

    # Put file in S3 SFTP location
    cloverleaf.upload_s3(filename, folder)

    # Check the S3 bucket iteratively when the file is picked by Cloverleaf
    s3_files = [file.split()[0].split(':')[1][len(folder):] for file in cloverleaf.get_s3_details(folder)]
    count = 0

    while filename in s3_files and count < TIME_LIMIT:
        count += 1
        time.sleep(1)
        s3_files = [file.split()[0].split(':')[1][len(folder):] for file in cloverleaf.get_s3_details(folder)]
        print(s3_files)

    if count == TIME_LIMIT:
        logging.error('Time limit of {} exceeded'.format(TIME_LIMIT))
    else:
        logging.info('File {} got picked up by Cloverleaf'.format(filename))

    # time.sleep(2)
    # logging.info('Starting the Phase II: Monitoring the S3 bucket after XLATE operation')
    # rabbitmq_s3 = 'syapse'
    #
    # rabbit = TestExecution(rabbitmq_s3, profile)
    # res_folder = ''
    # rabbit.get_s3_details(res_folder)

    del cloverleaf


if __name__ == '__main__':
    main()